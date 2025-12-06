import os
import re
from typing import Tuple, Dict

import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate

# Load env vars
load_dotenv()

# Page setup
st.set_page_config(
    page_title="Yukti • AI Agent",
    page_icon="logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Theme: Under the Moonlight
# Colors: #CCCCFF (Light), #A3A3CC (Mid), #5C5C99 (Mid-Dark), #292966 (Dark)
st.markdown("""
    <style>
    /* Global Settings */
    .stApp {
        background-color: #CCCCFF; 
    }
    
    /* Typography */
    h1, h2, h3, h4, h5, h6 { 
        color: #292966 !important; 
        font-family: 'Helvetica', sans-serif;
        font-weight: 700;
    }
    p, li, div, label, .stMarkdown {
        color: #292966 !important;
    }
    
    /* Chat Cards */
    .stChatMessage {
        background-color: #ffffff;
        border: 1px solid #5C5C99;
        box-shadow: 0 4px 6px rgba(41, 41, 102, 0.1);
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 12px;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #292966; 
        border-right: 1px solid #5C5C99;
    }
    [data-testid="stSidebar"] * {
        color: #CCCCFF !important;
    }

    /* Dark Mode Support */
    @media (prefers-color-scheme: dark) {
        .stApp { background-color: #292966 !important; }
        h1, h2, h3, h4, h5, h6 { color: #CCCCFF !important; }
        p, li, div, span, label, .stMarkdown { color: #A3A3CC !important; }
        
        .stChatMessage {
            background-color: #5C5C99 !important;
            border: 1px solid #A3A3CC !important; 
        }
        
        .stChatInput textarea {
            background-color: #5C5C99 !important;
            color: #ffffff !important;
            border: 1px solid #A3A3CC !important;
        }
    }

    /* Components */
    .stButton>button {
        background-color: #5C5C99; 
        color: #ffffff !important; 
        border: none;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #292966;
        border: 1px solid #CCCCFF;
        color: #CCCCFF !important;
    }

    /* Utility */
    header { background-color: transparent !important; }
    .stToolbar button { color: inherit !important; }
    </style>
""", unsafe_allow_html=True)

# Initialize Resources
@st.cache_resource
def load_vector_db():
    try:
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
        return Chroma(persist_directory="chroma_db", embedding_function=embeddings)
    except Exception as e:
        st.error(f"DB Error: {e}")
        st.stop()

@st.cache_resource
def load_llm():
    return ChatGroq(model="llama-3.1-8b-instant", temperature=0)

db = load_vector_db()
llm = load_llm()

FALLBACK_MSG = """I'm still learning. For official details, please contact:
\n📧 principal@ecajmer.ac.in
\n📧 principal.eca@rajasthan.gov.in
\n📞 +91-145-2971024"""

prompt = ChatPromptTemplate.from_template("""
You are Yukti, the AI Agent for Engineering College Ajmer (ECA).
Your role is to answer questions about the college using ONLY the information provided in the context below.

IMPORTANT INSTRUCTIONS:
1. Answer the question based ONLY on the context provided. Do not use any external knowledge.
2. Carefully search through the context for the specific information requested.
3. For person-specific queries (room numbers, emails, contact info), look for the person's name and extract the associated details from the same section.
4. **DETAILED RESPONSES:** Do not be brief or "concise." When answering, provide a **comprehensive and detailed explanation**. Include all relevant facts, figures, and context found in the documents to give a complete answer.
5. **PERSON DETAILS:** If the answer involves a specific person (faculty, Head of Department, or staff), ALWAYS include their **Email Address**, **Room Number**, and **Designation** if that information is available.
6. **FALLBACK:** If the context does not contain enough information to answer the question, YOU MUST EXACTLY SAY:
   "I'm still learning. For official details, please contact: 📧 principal@ecajmer.ac.in 📧 principal.eca@rajasthan.gov.in 📞 +91-145-2971024"
7. DO NOT make up answers, names, dates, or any details that are not in the context.
8. Be friendly and professional in your tone.

Context from college documents:
{context}

Question: {question}

Answer:
""")

def combine_docs(docs):
    return "\n\n".join(d.page_content for d in docs)

def preprocess_and_get_filter(query: str) -> Tuple[str, Dict]:
    query_low = query.lower()
    search_query = query
    filter_conditions = []
    
    # 1. Person/Faculty detection
    person_keywords = ["room", "email", "contact", "phone", "office"]
    has_person_kw = any(k in query_low for k in person_keywords)
    has_name_pattern = bool(re.search(r"\b[A-Z][a-z]+\s+[A-Z][a-z]+", query))
    
    # Check if we should force faculty type
    current_types = [str(fc) for fc in filter_conditions if "type" in str(fc)]
    if (has_person_kw or has_name_pattern) and not any("faculty" in t for t in current_types):
        if not any("type" in t for t in current_types):
            filter_conditions.append({"type": "faculty"})
    
    if has_person_kw:
        if "room" in query_low: search_query += " room number office location"
        if "email" in query_low: search_query += " email address contact"

    # 2. Department Mapping
    dept_map = {
        r"\b(cse|cs-it|computer science)\b": "computer_science",
        r"\b(ee|electrical)\b": "electrical_engineering",
        r"\b(ece|electronics)\b": "electronics_and_comm",
        r"\b(me|mechanical)\b": "mechanical_engineering",
        r"\b(ce|civil)\b": "civil_engineering"
    }
    
    for pattern, dept_key in dept_map.items():
        if re.search(pattern, query_low):
            # Expand acronyms in search query for better semantic match
            if "cse" in pattern: search_query = re.sub(r"\b(cse|cs-it)\b", "Computer Science", search_query, flags=re.IGNORECASE)
            elif "ee" in pattern: search_query = re.sub(r"\bee\b", "Electrical Engineering", search_query, flags=re.IGNORECASE)
            elif "ece" in pattern: search_query = re.sub(r"\bece\b", "Electronics and Communication", search_query, flags=re.IGNORECASE)
            elif "me" in pattern: search_query = re.sub(r"\bme\b", "Mechanical Engineering", search_query, flags=re.IGNORECASE)
            elif "ce" in pattern: search_query = re.sub(r"\bce\b", "Civil Engineering", search_query, flags=re.IGNORECASE)
            
            filter_conditions.append({"department": dept_key})
            break # Assume one dept per query usually

    # 3. Category/Type Mapping
    type_found = False
    
    # Faculty/People
    if re.search(r"\b(hod|head of department|people|faculty|professor|teacher)\b", query_low):
        search_query = re.sub(r"\bhod\b", "Head of Department", search_query, flags=re.IGNORECASE)
        filter_conditions.append({"type": "faculty"})
        type_found = True
    
    # Placements
    if re.search(r"\b(tpo|placement|recruiters|jyoti gajrani|recruitment|job)\b", query_low):
        search_query = re.sub(r"\btpo\b", "Training and Placement Officer", search_query, flags=re.IGNORECASE)
        filter_conditions.append({"type": "placements"})
        type_found = True
        
    # Other categories
    simple_maps = {
        r"\b(lab|labs|laboratories|laboratory)\b": "labs",
        r"\b(notice|circular|announcement|notification)\b": "notice",
        r"\b(fee|fees|structure|payment|tuition)\b": "academics",
        r"\b(cell|cells|ncc|nss|women-cell|greivance|grievance)\b": "cell_or_club",
        r"\b(hostel|hostels|accommodation|dormitory|girls hostel|boys hostel)\b": "hostel",
        r"\b(sport|sports|athletic|athletics|gym|fitness|competition|game|games)\b": "sports"
    }

    for pattern, doc_type in simple_maps.items():
        if re.search(pattern, query_low):
            filter_conditions.append({"type": doc_type})
            type_found = True

    # Fallback to academics if no specific type found but academic words exist
    if not type_found and re.search(r"\b(course|courses|program|admission|syllabus|department|departments|curriculum)\b", query_low):
        filter_conditions.append({"type": "academics"})

    # Construct ChromaDB filter
    metadata_filter = {}
    if len(filter_conditions) > 0:
        if len(filter_conditions) > 1:
            metadata_filter = {"$and": filter_conditions}
        else:
            metadata_filter = filter_conditions[0]
            
    return search_query, metadata_filter

def run_chain(query):
    processed_query, metadata_filter = preprocess_and_get_filter(query)
    
    # Try with filter first
    search_kwargs = {"k": 15}
    if metadata_filter:
        search_kwargs["filter"] = metadata_filter

    docs = db.similarity_search(processed_query, **search_kwargs)
    
    # Fallback: Search everything if filter yielded nothing
    if len(docs) == 0 and metadata_filter:
        docs = db.similarity_search(processed_query, k=15)

    context = combine_docs(docs)
    
    # Check if we actually found meaningful content
    if not context or len(context.strip()) < 10:
        return FALLBACK_MSG

    inputs = {"context": context, "question": query}
    response = llm.invoke(prompt.format(**inputs))
    return response.content if hasattr(response, "content") else str(response)

# -- Sidebar --
with st.sidebar:
    st.header("🎓 Yukti Bot")
    st.markdown("**AI Agent for Engineering College Ajmer**")
    st.markdown("---")
    
    st.subheader("💡 Try asking about:")
    st.markdown("""
    - **Faculty:** "Who is the HOD of CSE?"
    - **Placements:** "Who is the TPO head?"
    - **Hostels:** "What are the hostel rules?"
    - **Labs:** "Details about Mechanical labs"
    """)
    
    st.markdown("---")
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("Made with 🤖 for ECA Students")

# -- Main Layout --
col1, col2 = st.columns([1, 6])

with col1:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=100)
    else:
        st.markdown("## 🎓")

with col2:
    st.title("Yukti • AI Agent")
    st.markdown("### Your Campus. Your Answers.")

st.markdown("---")

# -- Chat Interface --
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if query := st.chat_input("How can I help you today?"):
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🤔"):
            try:
                answer = run_chain(query)
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                st.error(f"An error occurred: {e}")
🎓 Yukti - The Autonomous Campus Intelligence Agent

Agent.ai Hackathon Submission
An intelligent, context-aware RAG agent designed to solve the information chaos in educational institutions.

🚀 Overview

Yukti is not just a chatbot; it is an AI Agent that centralizes and intelligently retrieves college information. It solves the problem of students navigating hundreds of scattered PDF circulars, fragmented web pages, and notice boards to find simple answers.

By leveraging a Hybrid Query Router, Yukti dynamically switches between precise fact-checking and broad semantic search, ensuring zero hallucinations for critical data like faculty names and exam schedules.

🧠 The "Agentic" Architecture

Unlike standard RAG chatbots, Yukti uses a sophisticated routing system:

Intent Classification: The agent uses Llama 3.1 to analyze the user's question and determine the intent (e.g., "Faculty Query", "Lab Infrastructure", "General Admission Info").

Dynamic Retrieval Strategy: Based on the intent, it autonomously selects the best retrieval tool:

Precise Keyword Search: For factual queries like "Who is the HOD of CSE?", it bypasses vector search to read specific source files directly. This guarantees 100% accuracy.

Semantic Vector Search: For broad queries like "Tell me about the college culture," it uses a vector database (ChromaDB) with MMR (Maximal Marginal Relevance) to provide a diverse and comprehensive summary.

🛠️ Tech Stack

Orchestration: LangChain

Vector Database: ChromaDB (Persistent Storage)

LLM: Groq (Llama 3.1 8B Instant) - Selected for ultra-low latency response times.

Embeddings: Hugging Face (all-mpnet-base-v2) - Selected for high semantic accuracy.

Frontend: Streamlit - Chosen for rapid prototyping and clean, accessible UI.

Data Pipeline: Custom Python scripts for automated crawling and intelligent chunking.

⚡ Key Features

Zero-Hallucination Faculty Search: Custom logic ensures accuracy for staff names and roles.

Context-Aware Answers: Understands department-specific contexts (e.g., distinguishing between "CSE HOD" and "Mechanical HOD").

Fast & Free: Optimized to run entirely on high-speed, free-tier APIs for maximum accessibility in public education sectors.

Professional UI: Features a clean interface with helpful sidebar navigation and clear contact fallbacks.

📂 Project Structure

college-chatbot-agent/
├── app.py                  # Main application logic & Query Router
├── build_vector_db.py      # Data ingestion pipeline (chunking & indexing)
├── requirements.txt        # Dependency list
├── data_texts/             # Curated knowledge base (The "Brain")
│   ├── DEPARTMENTS/
│   └── TRAINING_&_PLACEMENTS/
└── chroma_db/              # Persistent Vector Database


🚀 How to Run Locally

Clone the repository:

git clone <your-repo-url>
cd college-chatbot-agent


Install dependencies:

python -m venv venv
# Activate venv (Windows: venv\Scripts\activate, Mac/Linux: source venv/bin/activate)
pip install -r requirements.txt


Set up Environment Variables:
Create a .env file and add your keys:

GROQ_API_KEY=gsk_...
LANGCHAIN_API_KEY=lsv2_...
LANGCHAIN_TRACING_V2=true


Build the Database:

python build_vector_db.py


Run the Agent:

streamlit run app.py


🔮 Future Roadmap

Phase 1 (Current): Prototype Agent with Hybrid Retrieval.

Phase 2: Integration with WhatsApp Business API for student access.

Phase 3: Multi-modal capabilities (reading image-based circulars).
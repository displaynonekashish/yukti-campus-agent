import os
import shutil
from pathlib import Path
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# Configuration
load_dotenv()
DATA_FOLDERS = ["data_texts"]
CHROMA_DIR = "chroma_db"
EMBEDDING_MODEL = "sentence-transformers/all-mpnet-base-v2"

def get_txt_files():
    """Generator to find all .txt files in the data folders."""
    for folder in DATA_FOLDERS:
        if not os.path.exists(folder):
            print(f"[Warn] Folder not found: {folder}")
            continue
        
        for root, _, files in os.walk(folder):
            for f in files:
                if f.endswith(".txt"):
                    yield Path(root) / f

def detect_doc_type(filename: str, path_str: str) -> str:
    """Categorizes the document based on filename and folder context."""
    fname = filename.lower()
    path_context = path_str.lower()
    combined = f"{fname} {path_context}"

    # Priority checks based on path context
    if "hostel" in combined: return "hostel"
    if "sport" in combined: return "sports"
    if "women" in combined or "women-cell" in combined: return "cell_or_club"
    if "placements" in combined or "tpo" in combined or "recruitment" in combined: return "placements"
    if "cell" in combined or "ncc" in combined or "nss" in combined: return "cell_or_club"

    # Filename specific checks
    if "people" in fname or "faculty" in fname: return "faculty"
    if "labs" in fname or "lab" in fname: return "labs"
    if "questions" in fname or "faq" in fname: return "faq"
    if "announcement" in fname or "circular" in fname or "notice" in fname: return "notice"
    if "achievement" in fname: return "achievement"
    if "gallery" in fname: return "gallery"
    if "time table" in fname or "schedule" in fname or "timetable" in fname: return "timetable"
    if "about" in fname: return "about_college"
    if "course" in fname or "fee" in fname or "admission" in fname or "syllabus" in fname: return "academics"
    
    return "general"

def detect_department(path_str: str, content: str) -> str:
    """
    Determines the department based on folder structure and content.
    Includes strict path checking for short codes (me, ee, ce).
    """
    # Normalize path for consistent folder checking
    path = path_str.lower().replace("\\", "/")
    content_lower = (path_str + " " + content).lower()

    # Core Departments
    if "cs-it" in content_lower or "computer science" in content_lower or "cse" in content_lower:
        return "computer_science"
    if "ece" in content_lower or "electronics" in content_lower:
        return "electronics_and_comm"
    
    # Strict check for folder names to avoid partial matches (e.g., 'me' in 'Department')
    if "/ee/" in path or "electrical" in content_lower:
        return "electrical_engineering"
    if "/me/" in path or "mechanical" in content_lower:
        return "mechanical_engineering"
    if "/ce/" in path or "civil" in content_lower:
        return "civil_engineering"

    # Other Units
    if "mba" in content_lower or "management" in content_lower: return "management"
    if "mca" in content_lower or "computer application" in content_lower: return "computer_application"
    if "administration" in content_lower or "principal" in content_lower: return "administration"
    if "training" in content_lower or "placement" in content_lower: return "training_and_placement"
    if "academics" in content_lower: return "academics"
    if "student" in content_lower: return "student_corner"
    if "hostel" in content_lower: return "hostel"
    if "about" in content_lower: return "about_college"

    return "general"

def build_database():
    files = list(get_txt_files())
    if not files:
        print("No .txt files found to index.")
        return

    print(f"Processing {len(files)} files...")

    # Initialize Splitters
    # Fact splitter: keeps lines together (good for rosters/tables)
    fact_splitter = CharacterTextSplitter(separator="\n", chunk_size=400, chunk_overlap=50)
    # General splitter: good for narrative text
    general_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

    all_docs = []

    for path in files:
        try:
            loader = TextLoader(str(path), encoding="utf-8")
            raw_docs = loader.load()
            
            doc_type = detect_doc_type(path.name, str(path))
            
            # Choose appropriate splitter strategy
            if doc_type in ["faculty", "labs", "timetable", "achievement"]:
                splitter = fact_splitter
            else:
                splitter = general_splitter
            
            splits = splitter.split_documents(raw_docs)

            # Enrich metadata
            for s in splits:
                content = s.page_content.strip()
                if not content: continue
                
                s.metadata = {
                    "source": str(path),
                    "folder": Path(path).parent.name,
                    "file": Path(path).name,
                    "type": doc_type,
                    "department": detect_department(str(path), s.page_content),
                }
                all_docs.append(s)

        except Exception as e:
            print(f"[Error] Failed to process {path.name}: {e}")

    if not all_docs:
        print("No valid document chunks to index.")
        return

    # Rebuild Vector Store
    print(f"Indexing {len(all_docs)} chunks into ChromaDB...")
    
    if os.path.exists(CHROMA_DIR):
        shutil.rmtree(CHROMA_DIR)

    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    
    Chroma.from_documents(
        documents=all_docs,
        embedding=embeddings,
        persist_directory=CHROMA_DIR
    )

    print(f"✅ Database successfully built at: {CHROMA_DIR}")

if __name__ == "__main__":
    build_database()
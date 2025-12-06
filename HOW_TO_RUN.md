# How to Run the Chatbot App

## Prerequisites

1. **Python 3.8+** installed
2. **Groq API Key** - Get one from [https://console.groq.com](https://console.groq.com)

## Step-by-Step Setup

### 1. Install Dependencies

Make sure you're in the project directory and have a virtual environment activated (recommended):

```bash
# If you haven't created a virtual environment yet:
python -m venv venv

# Activate it:
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies:
pip install -r requirements.txt
```

### 2. Set Up Environment Variables

Create a `.env` file in the project root directory with your Groq API key:

```bash
# Create .env file
# On Windows (PowerShell):
echo GROQ_API_KEY=your_api_key_here > .env

# On Windows (CMD):
echo GROQ_API_KEY=your_api_key_here > .env

# On Mac/Linux:
echo "GROQ_API_KEY=your_api_key_here" > .env
```

**Or manually create `.env` file with:**
```
GROQ_API_KEY=your_actual_groq_api_key_here
```

> **Note:** Replace `your_actual_groq_api_key_here` with your actual Groq API key from [Groq Console](https://console.groq.com)

### 3. Rebuild Vector Database (IMPORTANT!)

Since we fixed metadata issues, you need to rebuild the vector database:

```bash
python build_vector_db.py
```

This will:
- Process all text files from `data_texts/` and `data_pdf_texts/`
- Create embeddings and store them in `chroma_db/`
- Take a few minutes depending on your data size

### 4. Run the Streamlit App

```bash
streamlit run app.py
```

The app will:
- Open in your default browser automatically
- Usually at `http://localhost:8501`
- Show the chatbot interface

## Troubleshooting

### Issue: "Error loading Chroma database"
**Solution:** Run `python build_vector_db.py` first to create the vector database.

### Issue: "GROQ_API_KEY not found"
**Solution:** 
1. Make sure you created a `.env` file in the project root
2. Check that the file contains: `GROQ_API_KEY=your_key_here`
3. Restart the Streamlit app

### Issue: "No module named 'streamlit'"
**Solution:** Install dependencies: `pip install -r requirements.txt`

### Issue: App runs but gives wrong answers
**Solution:** 
1. Check the terminal/console for debug output showing retrieved documents
2. Make sure you rebuilt the vector database after the fixes
3. Try queries without specific department/type filters first

## Quick Test

Once the app is running, try these test queries:
- "What is the HOD of Computer Science department?"
- "Tell me about admissions"
- "What are the library hours?"
- "Information about placements"

## Stopping the App

Press `Ctrl+C` in the terminal where Streamlit is running.


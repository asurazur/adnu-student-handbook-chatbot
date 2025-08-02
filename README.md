# ADNU Student Handbook Chatbot
This is a Retrieval-Augmented Generation (RAG) chatbot designed to assist students, faculty, and staff in querying the **Ateneo de Naga University Student Handbook** using natural language. It combines semantic search with a powerful LLM (e.g., GPT-4) to generate accurate and contextual responses based on official handbook content.

---

## 🔍 Features

- Ask questions in plain English (e.g., "What is the dress code on campus?")
- Retrieves relevant sections from the official student handbook
- Generates context-aware, conversational answers
- Built with **LlamaIndex**, **OpenAI**, and **Streamlit**

---

## ⚙️ Tech Stack

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/) — for the web interface
- [LlamaIndex](https://www.llamaindex.ai/) — for document indexing and retrieval
- [OpenAI GPT-4](https://platform.openai.com/) — for response generation
- PDF/Markdown/Docx Loader (depends on your document format)

---

## 🚀 Getting Started

### 1. Clone the Repository
    
```bash
git clone https://github.com/asurazur/adnu-student-handbook-chatbot.git
cd adnu-rag-chatbot
```

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Prepare Student Handbook
Place the student handbook (PDF, text, or markdown format) inside a data/ folder.

Update the RAG indexing script (if needed) to point to the correct file.

### 4. Setup Environment Variables
Create a ```.env``` file 
OPENAI_API_KEY=your_openai_api_key

### 5. Run the App
```bash
streamlit run app.py
```
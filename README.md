# 🤖 GenAI Study & Career Assistant

An all-in-one Generative AI application combining **LLM integration, Prompt Engineering, Retrieval-Augmented Generation (RAG), Embeddings, Vector Database, AI Agents, and Tool Calling** into a single Streamlit application.

## 🚀 Project Overview

The **GenAI Study & Career Assistant** is a Generative AI application designed to help students with learning, career preparation, document-based question answering, and task management.

### ✨ Key Features

* 💬 **General AI Assistant** – Ask general questions and receive AI-generated responses.
* 📚 **Study Assistant** – Get beginner-friendly explanations for academic and technical topics.
* 💼 **Career Assistant** – Get guidance for internships, resumes, skills, and interviews.
* 📄 **Chat With Documents** – Upload a PDF and ask questions using RAG.
* 🤖 **AI Agent** – Performs tasks using tools such as calculator, task management, and current time.

---

## 🧠 Technologies Used

| Technology         | Purpose                           |
| ------------------ | --------------------------------- |
| Python             | Application development           |
| Streamlit          | Web interface                     |
| Google Gemini      | Large Language Model              |
| Prompt Engineering | Controlling AI responses          |
| RAG                | Document-based question answering |
| Embeddings         | Semantic representation of text   |
| FAISS              | Vector similarity search          |
| PyPDF              | PDF text extraction               |
| python-dotenv      | Environment variable management   |

---

# 📄 Retrieval-Augmented Generation (RAG)

The document question-answering system follows this pipeline:

```text
PDF Upload
     ↓
Text Extraction
     ↓
Text Cleaning
     ↓
Text Chunking
     ↓
Embeddings
     ↓
FAISS Vector Database
     ↓
Similarity Search
     ↓
Relevant Context
     ↓
Gemini LLM
     ↓
Answer
```

### 🔍 RAG Process

1. **PDF Upload** – The user uploads a PDF.
2. **Text Extraction** – Text is extracted from the document.
3. **Text Cleaning** – Unnecessary whitespace and empty content are removed.
4. **Text Chunking** – The document is divided into smaller overlapping chunks.
5. **Embeddings** – Text chunks are converted into numerical vector representations.
6. **Vector Database** – Embeddings are stored in FAISS.
7. **Similarity Search** – Relevant chunks are retrieved based on the user's question.
8. **Context Retrieval** – The relevant information is provided as context.
9. **Gemini LLM** – Gemini generates the final answer using the retrieved context.

### ⚙️ Chunk Configuration

```text
Chunk Size: 1000 characters
Overlap: 200 characters
```

---

# 🤖 AI Agent

The AI Agent understands the user's request and decides whether a tool should be used.

### 🛠️ Available Tools

* 🧮 **Calculator**
* 📝 **Add Task**
* 📋 **List Tasks**
* 🕐 **Current Time**

### 🔄 AI Agent Workflow

```text
Understand Task
      ↓
Analyze Request
      ↓
Decide Whether Tool Is Required
      ↓
Select Tool
      ↓
Execute Tool
      ↓
Process Result
      ↓
Generate Response
```

### Example

```text
User:
Calculate 25 * 18

        ↓

AI Agent
        ↓
Calculator Tool
        ↓
450
        ↓
"The answer is 450."
```

Another example:

```text
User:
Add Complete my capstone project to my tasks

        ↓

AI Agent
        ↓
Add Task Tool
        ↓
Task stored
        ↓
"Task added successfully"
```

---

# 🏗️ Project Architecture

```text
                    ┌──────────────────────────┐
                    │       Streamlit UI       │
                    └────────────┬─────────────┘
                                 │
             ┌───────────────────┼───────────────────┐
             │                   │                   │
             ↓                   ↓                   ↓
       General AI          Study/Career          AI Agent
             │                   │                   │
             │                   │              Tool Calling
             │                   │                   │
             │                   │          ┌────────┼────────┐
             │                   │          ↓        ↓        ↓
             │                   │     Calculator   Tasks    Time
             │                   │
             └───────────────────┼───────────────────┘
                                 ↓
                           Gemini LLM
                                 ↑
                                 │
                       ┌─────────┴─────────┐
                       │       RAG         │
                       └─────────┬─────────┘
                                 │
                            PDF Document
                                 ↓
                         Text Extraction
                                 ↓
                           Chunking
                                 ↓
                          Embeddings
                                 ↓
                        FAISS Vector DB
                                 ↓
                       Similarity Retrieval
                                 ↓
                        Relevant Context
                                 ↓
                           Gemini LLM
```

---

# 🗂️ Project Structure

```text
genai_capstone_assistant/
│
├── agent/
│   ├── __init__.py
│   ├── agent.py
│   ├── state.py
│   └── tools.py
│
├── core/
│   ├── __init__.py
│   ├── llm.py
│   └── prompts.py
│
├── rag/
│   ├── __init__.py
│   ├── document_processor.py
│   ├── embeddings.py
│   ├── qa.py
│   └── vector_store.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Arpitha-23/genai_capstone_assistant.git
cd genai_capstone_assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 API Configuration

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_gemini_api_key
```

The `.env` file is excluded from Git using `.gitignore`.

**Never upload your API key to GitHub.**

---

# ▶️ Run the Application

Run:

```bash
streamlit run app.py
```

The application will open in your browser.

Usually:

```text
http://localhost:8501
```

---

# 🧪 Testing

### 💬 General AI

```text
What is Generative AI?
```

### 📚 Study Assistant

```text
Explain DBMS normalization with an example.
```

### 💼 Career Assistant

```text
How can I prepare for a software development internship?
```

### 📄 Chat With Documents

Upload a PDF and ask:

```text
What is this document about?
```

### 🤖 AI Agent

```text
Calculate 15 * 7
```

```text
Add Complete my capstone project to my tasks
```

```text
Show my tasks
```

```text
What is the current time?
```

---

# 🔐 Security

The project uses environment variables for API key management.

The following are excluded using `.gitignore`:

```text
.env
venv/
```

No API keys should be committed to the repository.

---

# ⚠️ Limitations

* PDF processing works best with text-based PDFs.
* Scanned image-only PDFs may require OCR.
* Gemini API usage is subject to API quotas and rate limits.
* The task list is maintained in application memory.
* Vector data is maintained during the application session.

---

# 🔮 Future Enhancements

* Persistent database for tasks
* User authentication
* OCR support for scanned PDFs
* Multiple document support
* Conversation memory
* Cloud vector databases
* Additional external tools and APIs
* Voice interaction
* Resume analysis
* Personalized learning plans
* Production-grade deployment

---

# 🎯 Learning Outcomes

This project demonstrates practical understanding of:

* Large Language Models
* Generative AI
* Prompt Engineering
* Retrieval-Augmented Generation
* Text Chunking
* Embeddings
* Vector Databases
* Semantic Search
* AI Agents
* Function / Tool Calling
* Agent State Management
* Streamlit Application Development
* Gemini API Integration

---

# 📸 Screenshots

Application screenshots can be added here to demonstrate the different modes.

Recommended screenshots:

```text
screenshots/
├── general_ai.png
├── study_assistant.png
├── career_assistant.png
├── document_qa.png
└── ai_agent.png
```

---

# 🌐 Live Demo

👉 **[Open the Live Application](https://genaicapstoneassistant-rguzaedljncs2xfq6ccwwr.streamlit.app/)**

---

# 💻 GitHub Repository

👉 **[View Source Code](https://github.com/Arpitha-23/genai_capstone_assistant)**

---

# 👩‍💻 Author

**Arpitha Gowda**

Computer Science & Engineering Student

---

# ⭐ Project Highlights

This capstone combines multiple Generative AI concepts into one practical application:

```text
LLM
 +
Prompt Engineering
 +
RAG
 +
Embeddings
 +
Vector Database
 +
AI Agents
 +
Tool Calling
 =
GenAI Capstone Application
```

---

## 📌 Capstone Project

Developed as part of a Generative AI learning program covering:

**LLMs → RAG → AI Agents → GenAI Application Development**

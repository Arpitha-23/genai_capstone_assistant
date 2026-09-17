# 🤖 GenAI Study & Career Assistant

An all-in-one Generative AI application that combines **LLM integration, Prompt Engineering, Retrieval-Augmented Generation (RAG), Embeddings, Vector Database, AI Agents, and Tool Calling** into a single Streamlit application.

---

## 🚀 Project Overview

The **GenAI Study & Career Assistant** is designed to help students with learning, career preparation, document-based question answering, and task management.

The application provides multiple AI-powered modes:

- 💬 General AI Assistant
- 📚 Study Assistant
- 💼 Career Assistant
- 📄 Chat With Documents
- 🤖 AI Agent

The project demonstrates the integration of multiple Generative AI concepts into one practical application.

---

## ✨ Features

### 💬 General AI Assistant

Users can ask general questions and receive AI-generated responses using the Gemini LLM.

### 📚 Study Assistant

Provides beginner-friendly explanations for:

- Computer Science concepts
- Academic topics
- Interview preparation
- Technical questions
- Revision topics

### 💼 Career Assistant

Helps students with:

- Internship preparation
- Career guidance
- Resume-related questions
- Interview preparation
- Technical skill development

### 📄 Chat With Documents

Users can upload a PDF and ask questions about its contents.

The application performs:

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

🤖 AI Agent

The AI Agent understands the user's request and decides whether a tool should be used.

Available tools include:

🧮 Calculator
📝 Add Task
📋 List Tasks
🕐 Current Time

🧠 Technologies Used
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

🏗️ Project Architecture

                    ┌──────────────────────────┐
                    │        Streamlit UI      │
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

🤖 AI Agent Workflow

The AI Agent follows this workflow:
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

🗂️ Project Structure
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

🔮 Future Enhancements

Possible future improvements include:

Persistent database for user tasks
User authentication
OCR support for scanned PDFs
Multiple document support
Conversation memory
Cloud vector databases
More external tools and APIs
Voice interaction
Resume analysis
Personalized learning plans
Production-grade deployment

🎯 Learning Outcomes

This project demonstrates practical understanding of:

Large Language Models
Generative AI
Prompt Engineering
Retrieval-Augmented Generation
Text Chunking
Embeddings
Vector Databases
Semantic Search
AI Agents
Function/Tool Calling
Agent State Management
Streamlit Application Development
Gemini API Integration

🌐 Live Demo

Live Website:https://genaicapstoneassistant-rguzaedljncs2xfq6ccwwr.streamlit.app/

💻 GitHub Repository

Source Code:https://github.com/Arpitha-23/genai_capstone_assistant

👩‍💻 Author

Arpitha Gowda
Computer Science & Engineering Student
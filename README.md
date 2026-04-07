# RAG-Based Chatbot 🤖

## Overview
This project implements a Retrieval-Augmented Generation (RAG) chatbot that answers user queries strictly based on a provided knowledge base.

The chatbot retrieves relevant document chunks and generates answers using a HuggingFace Seq2Seq model (FLAN-T5), ensuring responses are grounded in context and avoiding hallucinations.

---

## Features
- Supports PDF, TXT, HTML documents
- Context-based answering (no hallucination)
- Displays sources of answers
- Uses FAISS for vector storage
- Uses HuggingFace Transformers (no OpenAI dependency)

---

## Architecture
User Query → Retriever → Relevant Documents → LLM → Answer + Sources

---

## Tech Stack
- Python
- LangChain (for document processing & retrieval)
- FAISS (vector database)
- HuggingFace Transformers (FLAN-T5)

---

## Setup

1. Install dependencies
pip install -r requirements.txt

2. Add documents
Place your documents inside:
data/docs/

Supported formats:
PDF
TXT
HTML

3. Run the chatbot
python app.py

Example Queries:
What is the company leave policy?
What are the working hours?
Can employees work remotely?

<!-- Future Improvements
Add Streamlit UI
Improve answer formatting
Add chat history
Deploy using Docker -->
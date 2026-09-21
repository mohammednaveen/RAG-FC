# RAG - FC

A practical introduction to **Retrieval-Augmented Generation (RAG)**, starting with a simple RAG implementation and progressing to an e-commerce customer-support chatbot using **Pinecone** and **OpenRouter**.

---

## Table of Contents
- [1. Clone the Repository](#1-clone-the-repository)
- [2. Install Python 3.11](#2-install-python-311)
- [3. Create a Virtual Environment](#3-create-a-virtual-environment)
- [4. Install Dependencies](#4-install-dependencies)
- [5. Configure API Keys](#5-configure-api-keys)
- [6. Run the Simple RAG](#6-run-the-simple-rag)
- [7. Run the E-Commerce RAG](#7-run-the-e-commerce-rag)
- [Project Structure](#project-structure)
- [RAG Flow](#rag-flow)

---

## 1. Clone the Repository

Clone the repository and enter the project directory:

```bash
git clone [https://github.com/mohammednaveen/RAG-FC.git](https://github.com/mohammednaveen/RAG-FC.git)
cd RAG-FC
```

---

## 2. Install Python 3.11

This project uses Python 3.11.

### Windows

Install Python 3.11 from the terminal:

```cmd
winget install Python.Python.3.11
```

Close and reopen the terminal, then check the installed versions:

```cmd
py --list
```

### macOS

If Homebrew is already installed:

```bash
brew install python@3.11
```

If Homebrew is not installed, install it first:

```bash
/bin/bash -c "$(curl -fsSL [https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh](https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh))"
```

Then install Python 3.11:

```bash
brew install python@3.11
```

---

## 3. Create a Virtual Environment

### Windows

```cmd
py -3.11 -m venv rag_env
rag_env\Scripts\activate
```

### macOS / Linux

```bash
python3.11 -m venv rag_env
source rag_env/bin/activate
```

Verify the Python version:

```bash
python --version
```

You should see:
```text
Python 3.11.x
```

---

## 4. Install Dependencies

Make sure the virtual environment is activated, then install all required packages:

```bash
pip install -r requirements.txt
```

---

## 5. Configure API Keys

The project contains `.env` files with placeholder values. Replace the placeholders with your own credentials.

For the e-commerce project (`ecommerce-rag/.env`):

```dotenv
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX_NAME=your_pinecone_index_name
OPENROUTER_API_KEY=your_openrouter_api_key
```

> **Warning:** Never commit your actual `.env` file or share your API keys publicly.

---

## 6. Run the Simple RAG

From the root project directory:

```bash
python simple_rag.py
```

This demonstrates the basic RAG process:

```text
Documents
    ↓
Embeddings
    ↓
Similarity Search
    ↓
Relevant Information
    ↓
LLM
    ↓
Answer
```

---

## 7. Run the E-Commerce RAG

Navigate to the e-commerce directory:

```bash
cd ecommerce-rag
```

### Ingest Documents

Run the ingestion script to prepare the vector database:

```bash
python ingest.py
```

This step:
- Loads the documents
- Splits them into chunks
- Adds metadata
- Uploads the chunks and embeddings to Pinecone

### Start the Chatbot

Start the interactive chat interface:

```bash
python rag.py
```

You can now ask questions about:
- Products
- Prices
- Product specifications
- Shipping
- Returns
- Other information contained in the provided documents

---

## Project Structure

```text
RAG-FC/
│
├── simple_rag.py
├── requirements.txt
├── .env
├── .gitignore
│
└── ecommerce-rag/
    ├── .env
    ├── ingest.py
    ├── rag.py
    │
    └── data/
        ├── products.txt
        ├── returns.txt
        └── shipping.txt
```

---

## RAG Flow

```text
Documents
    ↓
Chunking
    ↓
Pinecone
    ↓
Retrieve Relevant Information
    ↓
Context + Question
    ↓
LLM
    ↓
Answer
```

---

The project starts with a simple RAG implementation to build a foundational understanding and scales up to a production-pattern customer support assistant.

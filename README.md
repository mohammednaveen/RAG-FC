RAG - FC

A practical introduction to Retrieval-Augmented Generation (RAG), starting with a simple RAG implementation and progressing to an e-commerce customer-support chatbot using Pinecone and OpenRouter.

1. Clone the Repository
git clone https://github.com/mohammednaveen/RAG-FC.git
cd RAG-FC
2. Install Python 3.11

This project uses Python 3.11.

Windows

Install Python 3.11 from the terminal:

winget install Python.Python.3.11

Close and reopen the terminal, then check:

py --list
macOS

If Homebrew is installed:

brew install python@3.11

If Homebrew is not installed:

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Then:

brew install python@3.11
3. Create a Virtual Environment
Windows
py -3.11 -m venv rag_env
rag_env\Scripts\activate
macOS
python3.11 -m venv rag_env
source rag_env/bin/activate

Verify the Python version:

python --version

It should show:

Python 3.11.x
4. Install Dependencies

With the virtual environment activated:

pip install -r requirements.txt
5. Configure API Keys

The project contains .env files with placeholder values.

Replace the placeholders with your own API keys.

For the e-commerce project:

PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX_NAME=your_pinecone_index_name
OPENROUTER_API_KEY=your_openrouter_api_key

Never share your actual API keys publicly.

6. Run the Simple RAG

From the main project directory:

python simple_rag.py

This demonstrates the basic RAG process:

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
7. Run the E-Commerce RAG

Move into the e-commerce project:

cd ecommerce-rag
Ingest the Documents
python ingest.py

This loads the documents, splits them into chunks, adds metadata, and uploads them to Pinecone.

Start the Chatbot
python rag.py

You can now ask questions about:

Products
Prices
Product specifications
Shipping
Returns
Other information contained in the provided documents
Project Structure
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
RAG Flow
Documents
    ↓
Chunking
    ↓
Pinecone
    ↓
Retrieve relevant information
    ↓
Context + Question
    ↓
LLM
    ↓
Answer

The project starts with a simple RAG implementation to understand the fundamentals and then applies those concepts to a practical e-commerce customer-support chatbot.

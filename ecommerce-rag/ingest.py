import os
from pathlib import Path

from dotenv import load_dotenv
from pinecone import Pinecone
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


# Load environment variables
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")


# Connect to Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX_NAME)

print("Connected to Pinecone!")


# Load documents
data_folder = Path("data")
documents = []

for file in data_folder.glob("*.txt"):

    text = file.read_text(encoding="utf-8")

    documents.append(
        Document(
            page_content=text,
            metadata={
                "source": file.name
            }
        )
    )

print(f"Loaded {len(documents)} documents")


# Split documents into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

records = []

for document in documents:

    chunks = splitter.split_text(document.page_content)

    for i, chunk in enumerate(chunks):

        records.append({
            "_id": f"{document.metadata['source']}-{i}",
            "text": chunk,
            "source": document.metadata["source"],
            "chunk_number": i
        })

print(f"Created {len(records)} chunks")


# Upload chunks to Pinecone
index.upsert_records(
    namespace="ecommerce",
    records=records
)

print("All chunks uploaded to Pinecone!")
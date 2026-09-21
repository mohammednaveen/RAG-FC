import os

from dotenv import load_dotenv
from pinecone import Pinecone
from openai import OpenAI


# Load environment variables
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


# Connect to Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX_NAME)


# Connect to OpenRouter
client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

conversation = []

# Start chatbot
print("\nE-commerce RAG Chatbot")
print("Type 'exit' to stop.\n")


while True:

    question = input("Customer: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break


    # Search Pinecone
    results = index.search(
        namespace="ecommerce",
        query={
            "inputs": {
                "text": question
            },
            "top_k": 3
        }
    )


    # Get relevant chunks
    matches = results["result"]["hits"]

    context = ""

    for match in matches:

        text = match["fields"]["text"]

        source = match["fields"].get(
            "source",
            "Unknown"
        )

        context += f"""
Source: {source}

{text}
"""
        
    conversation.append({
        "role": "user",
        "content": question
    })


    # Create prompt
    prompt = f"""
You are an e-commerce customer support assistant.

Answer the customer's question using ONLY
the information provided in the context.

If the answer cannot be found in the context,
say that you don't have enough information.

Conversation history:
{conversation}

Context:
{context}

Customer question:
{question}

Answer:
"""


    # Ask the LLM
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )


    # Display answer
    answer = response.choices[0].message.content

    print("\nBot:")
    print(answer)


    # Display sources
    print("\nSources:")

    for match in matches:

        source = match["fields"].get(
            "source",
            "Unknown"
        )

        print("-", source)

    print()
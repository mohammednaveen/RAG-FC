# sample pdf / document
documents = [
    "Students need at least 75% attendance.",
    "The library is open from 8 AM to 6 PM.",
    "The semester exam begins on December 10."
]


# For now, our RAG needs to do only three things:

# 1. Turn documents into vectors
# 2. Find the most relevant document
# 3. Give that document + question to an LLM

# get the embedding model :
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

# encode the sentence/text into embeddings/vectors
vectors = model.encode(documents)

print("Document vectors shape:", vectors.shape)

# this should give you something like : (3, 384) , which means:

# 3 documents
#    ↓
# 3 vectors
#    ↓
# each vector has 384 numbers

# example:
# Document 1 → [0.12, -0.43, 0.81, ... 384 numbers]
# Document 2 → [0.72,  0.11, -0.20, ... 384 numbers]
# Document 3 → [-0.31, 0.92, 0.17, ... 384 numbers]


# Now let's embed a question:
question = "Can I write the exam if my attendance is low?"

question_vector = model.encode([question])

# Now we will perform the actual retrieval:
# we will use cosine similarity
from sklearn.metrics.pairwise import cosine_similarity

similarities = cosine_similarity(
    question_vector,
    vectors
)

print("Similarity scores:", similarities)

# You might see something conceptually like:

# [[0.82, 0.15, 0.31]]

# that is :
# Question
#    │
#    ├── Attendance document → 0.82  ← highest
#    ├── Library document     → 0.15
#    └── Exam date document   → 0.31

best_index = similarities.argmax()

relevant_document = documents[best_index]

print(relevant_document)

# Now the A (augment) in RAG: 
# We are going to give this to an LLM

prompt = f"""
Use the following context to answer the question.

Context:
{relevant_document}

Question:
{question}

Answer:
"""

# send context + question to the LLM

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

answer = response.choices[0].message.content

print("\nFinal answer:")
print(answer)


# Our entire miniature RAG now looks like:

#               DOCUMENTS
#                   ↓
#               Embeddings
#                   ↓
#             Vector storage
#                   ↑
#                   │
# QUESTION → Embedding
#                   ↓
#           Similarity search
#                   ↓
#          Relevant document
#                   ↓
#           Question + Context
#                   ↓
#                  LLM
#                   ↓
#                ANSWER

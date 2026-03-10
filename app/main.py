import streamlit as st
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import ollama

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load vector database
index = faiss.read_index("vector_db.index")

# Load chunks
with open("chunks.txt", "r", encoding="utf-8") as f:
    chunks = f.readlines()

st.title("AI Research Assistant")

question = st.text_input("Ask a question about the document")

if question:

    query_vector = model.encode([question])
    query_vector = np.array(query_vector).astype("float32")

    distances, indices = index.search(query_vector, k=3)

    context = ""
    for i in indices[0]:
        context += chunks[i] + "\n"

    st.subheader("Retrieved Context")
    st.write(context)

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion:{question}"
            }
        ]
    )

    answer = response["message"]["content"]

    st.subheader("AI Answer")
    st.write(answer)
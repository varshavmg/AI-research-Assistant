import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# sample document chunks
chunks = [
    "Artificial Intelligence is transforming industries.",
    "AI systems can read documents.",
    "RAG systems combine search and language models.",
    "Machine learning improves systems with data."
]

# create embeddings
embeddings = model.encode(chunks)

# convert to numpy array
embeddings = np.array(embeddings)

# create FAISS index

def save_index_and_chunks(index_path="vector_db.index", chunks_path="chunks.txt"):
    """Persist the FAISS index and corresponding text chunks to disk."""
    faiss.write_index(index, index_path)
    with open(chunks_path, "w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(chunk.replace("\n", " ") + "\n")

# also call save at end of build (if running as script) later
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

# add embeddings to index
index.add(embeddings)

print("Vector database created!")

# save the index and chunks for later retrieval in assistant or pipeline
save_index_and_chunks()

def search(query, k=5):

    query_vector = model.encode([query])
    query_vector = np.array(query_vector)

    distances, indices = index.search(query_vector, k)

    results = [chunks[i] for i in indices[0]]

    return results

if __name__ == "__main__":

    # when run as script we already built & saved the index above
    question = "What is AI?"
    results = search(question)

    print("\nUser Question:", question)
    print("\nMost Relevant Chunks:")
    for r in results:
        print("-", r)


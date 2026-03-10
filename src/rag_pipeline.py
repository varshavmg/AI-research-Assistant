from document_loader import load_pdf
from text_splitter import split_text
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Step 1: Load PDF
pdf_path = "data/Attention_is_all_you_need.pdf"
document_text = load_pdf(pdf_path)
print("Document loaded successfully")

# Step 2: Split text into chunks
chunks = split_text(document_text, chunk_size=500, overlap=100)
print("Number of chunks:", len(chunks))

# Step 3: Save chunks to file 
with open("chunks.txt", "w", encoding="utf-8") as f:
    for chunk in chunks:
        f.write(chunk + "\n")

# Step 4: Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Step 5: Convert chunks into embeddings
embeddings = model.encode(chunks)
embeddings = np.array(embeddings).astype("float32")

# Step 6: Create FAISS vector database
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

print("Vector database created!")

# Step 7: Search function
def search(query, k=5):

    query_vector = model.encode([query])
    query_vector = np.array(query_vector).astype("float32")

    distances, indices = index.search(query_vector, k)

    results = [chunks[i] for i in indices[0]]

    return results


# Step 8: Ask questions
if __name__ == "__main__":

    question = input("Ask a question: ")

    results = search(question)

    print("\nMost Relevant Information:\n")

    for r in results:
        print("-", r)
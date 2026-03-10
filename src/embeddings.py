from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embeddings(chunks):
    
    embeddings = model.encode(chunks)

    return embeddings


if __name__ == "__main__":

    chunks = [
        "Artificial Intelligence is transforming industries.",
        "AI systems can read documents.",
        "RAG systems combine search and language models."
    ]

    vectors = create_embeddings(chunks)

    print("Number of embeddings:", len(vectors))
    print("\nFirst embedding vector:\n")
    print(vectors[0])
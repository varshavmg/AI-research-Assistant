def split_text(text, chunk_size=50, overlap=10):

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


if __name__ == "__main__":

    sample_text = """
    Artificial Intelligence is transforming industries worldwide.
    AI systems can read documents, understand context, and answer questions.
    Retrieval Augmented Generation systems combine search and language models.
    """

    chunks = split_text(sample_text, chunk_size=50, overlap=10)

    print("Number of chunks:", len(chunks))

    for i, chunk in enumerate(chunks):
        print(f"\nChunk {i+1}:")
        print(chunk)
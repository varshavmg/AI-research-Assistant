AI Research Assistant 🤖📄

An intelligent AI system that reads documents and answers questions using Retrieval-Augmented Generation (RAG). This project combines document processing, embeddings, and vector search for fast and context-aware answers.

🚀 Features
- Document Loading: Read PDFs and extract text efficiently.
- Text Chunking: Split large documents into smaller chunks for better retrieval.
- Embedding Generation: Convert text chunks into vector embeddings using all-MiniLM-L6-v2.
- Vector Database Search: Use FAISS for lightning-fast similarity search.
- RAG Pipeline: Retrieve relevant chunks and generate AI answers.

🏗 System Architecture
PDF → Text → Chunks → Embeddings → Vector Database → AI Answer

Pipeline Steps:
- Document Ingestion: Load PDFs and extract text.
- Chunking: Split text into smaller segments for semantic search.
- Embeddings: Generate vector representations for each chunk.
- Vector Store: Store embeddings in FAISS for similarity search.
- AI Answer Generation: Retrieve relevant chunks and answer questions using AI.

🧠 Model
Model Name: all-MiniLM-L6-v2

Property:	Value
Model Size:	~90MB
Vector Size:384 dimensions
Speed:Fast
Accuracy:Good
- Trained on millions of sentences, this model provides high-quality embeddings for semantic search.

📁 Project Structure:
ai-research-assistant/
├── data/                 # Store PDFs and processed text
├── src/                  # Core modules
│   ├── document_loader.py
│   ├── text_splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   └── rag_pipeline.py
├── app/                  # Application entry point
│   └── main.py
├── requirements.txt      # Python dependencies
├── README.md             # Documentation
└── architecture.png      # Architecture diagram

🌟 Future Improvements:
- FastAPI Web UI for interactive querying.
- Support multiple document formats (DOCX, TXT).
- Integration with larger LLMs for detailed answers.
- Streaming responses for faster feedback.
- Advanced RAG enhancements using LangChain pipelines.

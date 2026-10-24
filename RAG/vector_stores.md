- a vector store stores and retrieves data as numerical vectors (in memory or on disk)
- helps in similarity search
- enables fast similarity search on high dimensional vectors using indexing (eg. use clusters)
- used in semantic search, RAG, recommendation systems, image/multimedia systems

**Vector Store vs Vector Db**
- vector store (storage + retrieval) vector db (vector store + distributed, backup and restore, ACID, concurrency etc.)
- vector stores - FAISS
- vector dbs - Milvus, Qdrant, Pinecone etc.

**Vector stores in Langchain**
- here's an example of using Chroma for similarity search and other operations
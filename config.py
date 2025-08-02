# Constants for Configuration
CONFIG = {
    "chroma_persist_dir": "./chroma_store", # path to persist ChromaDB data
    "collection_name": "pdfs", # name of the collection in ChromaDB
    "chunk_size": 1000, # size of each chunk for text splitting
    "chunk_overlap": 250, # overlap between chunks to minimize context loss (1/4 of chunk size)
    "embedding_model": "text-embedding-3-small", # model for embeddings
    "llm_model": "gpt-4.1", # model for LLMs
    "similarity_top_k": 5, # number of similar nodes to retrieve
}

PROMPT="""
You are a helpful assistant. Use the context provided below to answer the user's question.
If the answer cannot be found in the context, say "I don't know based on the given context."

Context:
{context_str}

Question:
{query_str}
"""
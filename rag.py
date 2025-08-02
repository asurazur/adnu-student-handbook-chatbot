import os # For Environment Variables
from dotenv import load_dotenv
import chromadb # For ChromaDB
from llama_index.core import (
    VectorStoreIndex, # Wrapper for Vector Store Index
    SimpleDirectoryReader, # Read PDF Reader
    StorageContext, # For Storage Context
) # For Vector Store Index
from llama_index.vector_stores.chroma import ChromaVectorStore # For ChromaDB Vector Store
from llama_index.core.node_parser import TokenTextSplitter # For Chunking (Splitting) Text
from llama_index.embeddings.openai import OpenAIEmbedding # For OpenAI Embeddings
from llama_index.core.query_engine import RetrieverQueryEngine # For Query Engine
from llama_index.core.prompts import PromptTemplate # For Prompt Template
from config import CONFIG, PROMPT

# Set OpenAI API Key from Environment Variable
load_dotenv()

# Store in Vector Database
embed_model = OpenAIEmbedding(model=CONFIG["embedding_model"])

# Build Vector Database
# Chroma Client
chroma_client = chromadb.PersistentClient(
    path=CONFIG["chroma_persist_dir"]
) # Create Persistent Client for ChromaDB

chroma_collection = chroma_client.get_or_create_collection(
    name=CONFIG["collection_name"]
) # Avoid re-creation of collection

vector_store = ChromaVectorStore(
    chroma_collection=chroma_collection,
    embed_model=embed_model,
) # Create Vector Store with ChromaDB

storage_context = StorageContext.from_defaults(vector_store=vector_store) # Treat Vector Store as Storage Context

database = VectorStoreIndex.from_vector_store(
    vector_store=vector_store, # Use Vector Store
    embed_model=embed_model, # Use OpenAI Embedding Model
    storage_context=storage_context, # Use Storage Context
)

engine = database.as_query_engine(
    similarity_top_k=CONFIG["similarity_top_k"], # Number of similar nodes to retrieve
    text_qa_template=PromptTemplate(
        PROMPT, # Use the prompt from config
    )
)

if __name__ == "__main__":
    while True:
        user_query = input("Query: ") # Get User Query

        response = engine.query(
            user_query, # Query the engine with the user's question
        )
        
        print("Response:", response) # Print the response from the query engine
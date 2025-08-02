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
from config import CONFIG # Import Configuration Constants

# Set OpenAI API Key from Config
load_dotenv()

# Read the PDF
documents = SimpleDirectoryReader(
    input_files=["data/College-Student-Handbook-2017.pdf"], # Path to the PDF files
).load_data()


# Chunk the text
splitter = TokenTextSplitter(
    chunk_size=CONFIG['chunk_size'], # Size of each chunk
    chunk_overlap=CONFIG['chunk_overlap'], # Overlap between chunks
)
nodes = splitter.get_nodes_from_documents(documents)

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

# Treat Vector Store as Storage Context
storage_context = StorageContext.from_defaults(vector_store=vector_store) 

# Store nodes in Vector Database
VectorStoreIndex(
    nodes=nodes,
    embed_model=embed_model, # Use OpenAI Embedding Model
    storage_context=storage_context, # Use Storage Context
).set_index_id("college_handbook") # Set Index ID

from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

from langchain_cohere import CohereEmbeddings

load_dotenv()
# Initialize embeddings
def get_embeddings():
    return CohereEmbeddings(
        model="embed-english-v3.0",
        cohere_api_key=os.getenv("COHERE_API_KEY")
    )

# Pinecone API key
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = "firstindex"
def setup_vector_store():
    # Initialize embeddings
    embeddings = get_embeddings()
    
    # Connect to Pinecone
    pc = Pinecone(api_key=PINECONE_API_KEY)
    index = pc.Index(PINECONE_INDEX_NAME)
    
    # Create vector store
    return PineconeVectorStore(embedding=embeddings, index=index)

# Create a singleton instance of the vector store
vector_store = setup_vector_store()
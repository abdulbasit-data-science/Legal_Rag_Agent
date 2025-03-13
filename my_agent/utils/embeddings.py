from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from config import get_embeddings, PINECONE_API_KEY, PINECONE_INDEX_NAME

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
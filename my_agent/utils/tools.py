from my_agent.utils.embeddings import vector_store



from langchain_core.tools import tool


@tool(response_format="content_and_artifact")
def retrieve(query: str):
    """Retrieve information related to a query."""
    retrieved_docs = vector_store.max_marginal_relevance_search(query, k=5)
    
    # Create a formatted string of the retrieved content for readability
    serialized = "\n\n".join(
        (f"Source: {doc.metadata}\n" f"Content: {doc.page_content}")
        for doc in retrieved_docs
    )
    
    return serialized, retrieved_docs

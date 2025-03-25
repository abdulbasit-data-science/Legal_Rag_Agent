# src/__init__.py

# Package metadata
__version__ = "0.1.0"
__author__ = "Abdul basit"
__description__ = "Legal RAG Agent using LangChain and LangGraph"

# Import key components to make them directly accessible

from .embeddings import vector_store  
from .tools import retriever_tool  # Import specific tools
from .nodes import agent, rewrite, generate, grade_documents  # Import node functions
from .state import AgentState  # Import the state definition
from .graph import graph  # Import the compiled graph


import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables when the package is imported


# Define what’s exposed when someone does `from src import *`
__all__ = [
    
    
    "vector_store",
    "retriever_tool",
    "agent",
    "rewrite",
    "generate",
    "grade_documents",
    "AgentState",
    "graph",
]
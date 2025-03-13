# LangGraph RAG Application

A modular implementation of a Retrieval-Augmented Generation (RAG) system using LangGraph, Pinecone, and LangChain.

## Project Structure

```
project/
├── __init__.py        # Package initialization
├── config.py          # Environment variables and configuration
├── embeddings.py      # Vector store and embedding setup
├── tools.py           # Tool definitions
├── nodes.py           # Node functions for the graph
├── graph.py           # Graph definition and construction

```

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your API keys:
   ```
   GOOGLE_API_KEY=your_google_api_key
   COHERE_API_KEY=your_cohere_api_key
   PINECONE_API_KEY=your_pinecone_api_key
   ```

## Usage

```python
from main import run_conversation

# Run a conversation with a query
result = run_conversation("What can you tell me about quantum computing?")

# Print the results
for message in result:
    print(f"{message.type.upper()}: {message.content}")
```

## Components

- **config.py**: Handles environment variables and core components
- **embeddings.py**: Sets up vector store and embeddings
- **tools.py**: Contains tool definitions
- **nodes.py**: Defines node functions for the graph
- **graph.py**: Builds and configures the LangGraph


## License

[Add your license here]
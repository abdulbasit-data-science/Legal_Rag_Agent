# Legal RAG Agent

A modular, professional-grade legal assistant built with **LangChain**, **LangGraph**, and **Streamlit**. This project implements a Retrieval-Augmented Generation (RAG) agent designed to assist with legal queries by retrieving and generating responses based on legal documents and knowledge bases.

## Features
- Interactive web interface powered by Streamlit
- Modular graph-based architecture using LangGraph
- Retrieval-Augmented Generation (RAG) for legal document processing
- Configurable via environment variables
- Extensible design for adding new tools and nodes

## Project Structure
```
project/
├── src/                    # Core package containing application logic
│   ├── __init__.py        # Marks src as a Python package          # Configuration and environment variables
│   ├── embeddings.py      # Vector store and embedding setup
│   ├── tools.py           # Tool definitions (e.g., retriever_tool)
│   ├── nodes.py           # Node functions for the graph (agent, rewrite, etc.)
│   ├── state.py           # State definition (AgentState)
│   └── graph.py           # Graph definition and compilation
├── app.py                 # Streamlit application entry point
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables (not tracked in git)
├── README.md              # This file
└── .gitignore             # Git ignore file
```

## Prerequisites
- Python 3.8+
- Git (optional, for cloning the repository)
- A terminal or IDE (e.g., VS Code, PyCharm)

## Setup Instructions

1. **Clone the Repository** :
   ```bash
   git clone https://github.com/abdulbasit-data-science/Legal_Rag_Agent.git
   cd legal-rag-agent
   ```

2. **Create a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Copy the `.env.example` (if provided) to `.env` or create a new `.env` file:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` with your API keys or configuration (e.g., for embeddings or LLMs):
     ```
     API_KEY=your-api-key-here
     
     ```

5. **Run the Application**:
   ```bash
   streamlit run app.py
   ```
   - Open your browser to `http://localhost:8501` to interact with the Legal RAG Agent.

## Usage
- Launch the app using the command above.
- Type a legal query in the input box (e.g., "What is state court?").
- The agent will retrieve relevant legal information and generate a response based on its knowledge base.

## Development

### Adding New Tools
1. Edit `src/tools.py` to define new tools (e.g., legal document retriever) using the `@tool` decorator.
2. Update `src/graph.py` to include the new tool in the `ToolNode`.

### Adding New Nodes
1. Add new functions to `src/nodes.py` (e.g., for legal-specific processing).
2. Modify the graph in `src/graph.py` to incorporate the new nodes and edges.

### Testing
- Use a testing framework like `pytest` (add `pytest` to `requirements.txt` if needed).
- Example test command:
  ```bash
  pytest tests/
  ```

## Dependencies
Key libraries used (see `requirements.txt` for full list):
- `streamlit`: Web interface
- `langchain`: LLM and RAG integration
- `langgraph`: Graph-based workflow
- `python-dotenv`: Environment variable management

## Contributing
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature-name`.
3. Commit your changes: `git commit -m "Add your feature"`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Open a pull request.

## Acknowledgments
- Built with tools from [LangChain](https://github.com/langchain-ai/langchain), and [Streamlit](https://streamlit.io/).
- Inspired by RAG architectures for domain-specific applications.

## Contact
For questions or issues, please open an issue on GitHub or contact abdulbasit.sarfaraz@gmail.com.



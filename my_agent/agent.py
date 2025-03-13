from langgraph.graph import END
from langgraph.prebuilt import tools_condition
from langgraph.graph import MessagesState, StateGraph
from utils.nodes import query_or_respond, tools, generate
# Build the graph
graph_builder = StateGraph(MessagesState)
graph_builder.add_node(query_or_respond)
graph_builder.add_node(tools)
graph_builder.add_node(generate)

graph_builder.set_entry_point("query_or_respond")
graph_builder.add_conditional_edges(
    "query_or_respond",
    tools_condition,
    {END: "generate", "tools": "tools"},
)
graph_builder.add_edge("tools", "generate")
graph_builder.add_edge("generate", END)

from langgraph.checkpoint.memory import MemorySaver

# Using MemorySaver without the config_keys parameter
memory = MemorySaver()

# Compile the graph with the checkpointer
graph = graph_builder.compile(checkpointer=memory)

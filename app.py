from src.graph import graph

import streamlit as st
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from langchain_core.messages import HumanMessage, AIMessage

# Streamlit UI
st.title("🤖 Legal Rag Agent")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi,How can i help you?"}
    ]

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Handle user input
if prompt := st.chat_input(placeholder="Write your question here"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        
        # Prepare the input for the graph
        input_messages = [
            HumanMessage(content=msg["content"]) if msg["role"] == "user"
            else AIMessage(content=msg["content"])
            for msg in st.session_state.messages
        ]
        
        # Run the graph
        config = {"callbacks": [st_cb]}
        result = graph.invoke({"messages": input_messages}, config)
        
        # Extract the response from the result
        response = result["messages"][-1].content
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)

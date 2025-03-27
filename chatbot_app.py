from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
from typing import Annotated
from typing_extensions import TypedDict
from langchain_core.messages import HumanMessage, AIMessage
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

# Initialize the chat model
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="gemma2-9b-it",
    temperature=0.7
)

# Define state type
class State(TypedDict):
    messages: Annotated[list, add_messages]

# Create graph
graph_builder = StateGraph(State)

# Define chatbot function
def chatbot(state):
    return {"messages": llm.invoke(state["messages"])}

# Add node and edges
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

# Compile graph
graph = graph_builder.compile()

# Streamlit UI
st.title(" LangGraph Chatbot")

# Add sidebar
with st.sidebar:
    st.markdown("""
    ### About this Chatbot
    This is an AI chatbot built with:
    - LangGraph for workflow management
    - Groq's Gemma-2-9b-it model
    - Streamlit for the user interface
    
    The chatbot uses a simple graph structure:
    ```
    START -> chatbot -> END
    ```
            """)
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)
    else:
        with st.chat_message("assistant"):
            st.write(message.content)

# Get user input
if prompt := st.chat_input("Type your message here..."):
    # Add user message
    st.session_state.messages.append(HumanMessage(content=prompt))
    
    # Get response
    with st.spinner("Thinking..."):
        result = graph.invoke({"messages": st.session_state.messages})
        st.session_state.messages = result["messages"]
    
    st.rerun() 
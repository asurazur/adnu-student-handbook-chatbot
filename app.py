# streamlit_chatbot.py
import os
from dotenv import load_dotenv
import streamlit as st
from llama_index.llms.openai import OpenAI
from llama_index.core.llms import ChatMessage, MessageRole
from rag import engine

# Set your OpenAI API key
load_dotenv()
client = OpenAI(model="gpt-4.1")

st.set_page_config(page_title="Student Handbook Chatbot", page_icon="📕", layout="centered")

st.title("Student Handbook Chatbot")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    if msg.role == MessageRole.USER:
        st.chat_message("user").markdown(msg.content)
    elif msg.role == MessageRole.ASSISTANT:
        st.chat_message("assistant").markdown(msg.content)

# User input
if prompt := st.chat_input("Type your message here..."):
    # Add user message
    user_msg = ChatMessage(role=MessageRole.USER, content=prompt)
    st.session_state.messages.append(user_msg)
    st.chat_message("user").markdown(prompt)

    # Get AI response
    with st.spinner("Thinking..."):
        response = engine.query(prompt)
        ai_msg = ChatMessage(role=MessageRole.ASSISTANT, content=response)

    # Add response to history
    st.session_state.messages.append(ai_msg)
    st.chat_message("assistant").markdown(response)
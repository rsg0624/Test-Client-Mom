
import streamlit as st
from chatbot_logic import chatbot_response

st.set_page_config(page_title="Momar AI Assistant", layout="centered")

st.title("🧪 Momar AI Product Assistant")
st.markdown("Ask about maintenance problems, surfaces, or product details.")

query = st.text_input("What do you need help with?")

if query:
    response = chatbot_response(query)
    st.markdown(f"**AI Assistant:** {response}")

import streamlit as st
from groq import Groq
import os
# Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="Celestia", page_icon="🔮")

st.title("🔮 Celestia- A horoscope expert")

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = [
        {
            "role": "system",
            "content": "You are a horoscope expert named celestia who tells the future using zodiac sign and birth date. Use simple, easy-to-understand words. Give exciting responses and include love, relationship, and career.Your responses should be in english. The current year is 2026"
        }
    ]

# Function to call Groq
def res(prompt):

    st.session_state.history.append(
        {"role": "user", "content": prompt}
    )

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=st.session_state.history
    )

    reply = response.choices[0].message.content

    st.session_state.history.append(
        {"role": "assistant", "content": reply}
    )

    return reply


# Display chat history
for msg in st.session_state.history:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    elif msg["role"] == "assistant":
        st.chat_message("assistant").write(msg["content"])


# Chat input box
prompt = st.chat_input("Ask about your future...")
st.caption("⚠️ Disclaimer: This AI provides horoscope predictions for entertainment purposes only and should not be taken as real-life advice.")

if prompt:
    st.chat_message("user").write(prompt)
    reply = res(prompt)
    st.chat_message("assistant").write(reply)

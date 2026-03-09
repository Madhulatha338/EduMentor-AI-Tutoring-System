# ======================================
# app.py — EduMentor (Cloud + Local Voice Support)
# ======================================

import os
import streamlit as st
from PIL import Image
from api_handler import send_query_get_response
from chat_gen import generate_html

# ==============================
# Voice Assistant Import (Safe Mode)
# ==============================
try:
    from voice_assistant import listen, speak
    VOICE_AVAILABLE = True
except Exception:
    VOICE_AVAILABLE = False


# ==============================
# App Setup
# ==============================
st.set_page_config(page_title="EduMentor AI Tutor", page_icon="🎓", layout="wide")

# Load logo
try:
    logo = Image.open("logo.png")
except:
    logo = None


# ==============================
# Header
# ==============================
c1, c2 = st.columns([0.9, 3.2])

with c1:
    if logo:
        st.image(logo, width=120)

with c2:
    st.title("EduMentor : An AI-Enhanced Tutoring System")

st.markdown("## 🧠 AI Tutor Description")
st.markdown(
"""
EduMentor simulates an intelligent AI tutor that helps students learn and review
subjects like **Science**, **Mathematics**, and **Geography**.

This demo version supports:
- Text based tutoring
- File based learning
- Optional voice interaction (local environments only)
"""
)

# Offline info
st.success("✅ EduMentor Tutor Ready")

# ==============================
# File Upload
# ==============================
st.subheader("📚 Upload Study Material (Optional)")

uploaded_file = st.file_uploader(
    "Upload your study material (PDF, TXT)",
    type=["pdf", "txt"]
)

if uploaded_file is not None:

    save_path = os.path.join(os.getcwd(), uploaded_file.name)

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"✅ File '{uploaded_file.name}' uploaded successfully!")

    st.session_state["uploaded_file_path"] = save_path

else:
    st.session_state.setdefault("uploaded_file_path", None)


# ==============================
# Sidebar
# ==============================
st.sidebar.header("EduMentor AI Tutor")

if logo:
    st.sidebar.image(logo, width=120)

if VOICE_AVAILABLE:
    st.sidebar.success("🎤 Voice assistant enabled (local mode)")
else:
    st.sidebar.info("💬 Voice assistant disabled in cloud mode")

# Download chat history
if st.sidebar.button("📄 Generate Chat History"):

    if "messages" in st.session_state and len(st.session_state.messages) > 0:

        html_data = generate_html(st.session_state.messages)

        st.sidebar.download_button(
            label="⬇️ Download Chat History",
            data=html_data,
            file_name="EduMentor_Chat_History.html",
            mime="text/html"
        )

    else:
        st.sidebar.warning("No chat messages yet!")


# ==============================
# Chat Section
# ==============================
st.subheader("💬 Q&A with AI Tutor")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ==============================
# Text Question Input
# ==============================
prompt = st.chat_input("Ask your question here...")


# ==============================
# Voice Input (Local Only)
# ==============================
if VOICE_AVAILABLE:

    if st.button("🎤 Ask Question by Voice"):

        st.info("Listening... Please speak.")

        voice_prompt = listen()

        if voice_prompt:

            st.write("🗣️ You asked:", voice_prompt)

            st.session_state.messages.append(
                {"role": "user", "content": voice_prompt}
            )

            with st.chat_message("user"):
                st.markdown(voice_prompt)

            with st.chat_message("assistant", avatar="👨🏻‍🏫"):

                message_placeholder = st.empty()

                with st.spinner("Thinking..."):

                    response = send_query_get_response(
                        None,
                        voice_prompt,
                        file_path=st.session_state.get("uploaded_file_path")
                    )

                    message_placeholder.markdown(response)

                    st.session_state.messages.append(
                        {"role": "assistant", "content": response}
                    )

                    speak(response)


# ==============================
# Text Question Handling
# ==============================
if prompt:

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="👨🏻‍🏫"):

        message_placeholder = st.empty()

        with st.spinner("Thinking..."):

            response = send_query_get_response(
                None,
                prompt,
                file_path=st.session_state.get("uploaded_file_path")
            )

            message_placeholder.markdown(response)

            st.session_state.messages.append(
                {"role": "assistant", "content": response}
            )

            if VOICE_AVAILABLE:
                speak(response)


# ==============================
# Footer
# ==============================
st.divider()

st.caption(
"🎓 EduMentor © 2025 | Built with ❤️ using Python & Streamlit"
)

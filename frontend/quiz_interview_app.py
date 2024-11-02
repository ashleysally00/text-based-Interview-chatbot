import streamlit as st
import requests
from gemini_interviewer import interview_process  # Import interview logic

st.title("Interactive Quiz and Chatbot App")

# Interview Section
st.header("Mock Interview")
interview_process()  # Call the interview function from gemini_interviewer.py

# Quiz Submission Section
st.header("Submit Your Quiz Response")
user_id = st.text_input("User ID")
question = st.text_input("Question")
answer = st.text_input("Answer")

if st.button("Submit Quiz Response"):
    response = {
        "user_id": user_id,
        "question": question,
        "answer": answer,
    }
    try:
        res = requests.post("http://localhost:5000/quiz/response", json=response)
        res.raise_for_status()  # Raise an error if the request failed
        st.write(res.json())
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")

# View All Quiz Responses Section
st.header("View All Quiz Responses")
if st.button("Get Quiz Responses"):
    try:
        res = requests.get("http://localhost:5000/quiz/responses")
        res.raise_for_status()
        responses = res.json()
        st.write(responses)
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")

# Speech-to-Text Section
st.header("Upload Audio for Speech Processing")
audio_file = st.file_uploader("Upload an audio file", type=["wav", "flac"])

if audio_file and st.button("Process Speech"):
    files = {"file": audio_file.getvalue()}
    try:
        res = requests.post("http://localhost:5000/process-speech", files=files)
        res.raise_for_status()
        st.write(res.json())
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")

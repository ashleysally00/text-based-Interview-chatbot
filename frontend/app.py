import streamlit as st
import google.generativeai as genai  # Import the Google Generative AI SDK
import os  # To retrieve the API key from environment variables
from gemini_interviewer import analyze_response_and_prompt_next_question, start_interview  # Import necessary functions

# Access the Gemini API key from Streamlit secrets
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

if not GEMINI_API_KEY:
    st.error("Gemini API key not found. Please check your Streamlit secrets.")
else:
    genai.configure(api_key=GEMINI_API_KEY)

# Streamlit Page Configuration
st.set_page_config(
    page_title="Interactive Mock Interview",
    page_icon="👔",
    layout="wide"
)

# Load custom CSS
def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Initialize session states
if "current_prompt" not in st.session_state:
    st.session_state.current_prompt = start_interview()  # Start with the initial question
if "user_response" not in st.session_state:
    st.session_state.user_response = ""

# App Title
st.title("Interactive Mock Interview")

# Input fields for user information
st.subheader("Please enter your details:")
age = st.number_input("Age:", min_value=0, max_value=120, value=0)  # Default value set to 0
gender = st.selectbox("Gender:", options=["", "female", "male", "other"])  # Default to blank
location = st.text_input("Location:", value="")  # Default blank
current_job_type = st.text_input("Current Job Type:", value="")  # Default blank
new_job_type = st.text_input("New Job Type:", value="")  # Default blank

# Display the current prompt/question with custom styling above the input field
st.markdown(
    f'<div class="interviewer-question">'
    f'<strong>Interviewer:</strong> {st.session_state.current_prompt}'
    f'</div>',
    unsafe_allow_html=True
)

# Use a single widget for user response
def submit():
    st.session_state.user_response = st.session_state.widget  # Store the response
    st.session_state.widget = ""  # Clear the response field

# Input field for user's response
st.text_area("Your response:", key="widget", height=150, on_change=submit)

# Submit button logic
if st.button("Submit"):
    if not st.session_state.user_response.strip():
        st.warning("Please provide a response before submitting.")
    else:
        # Call the function from gemini_interviewer to analyze the response and generate the next question
        try:
            # Generate the next question based on the user's response
            feedback_and_question = analyze_response_and_prompt_next_question(st.session_state.user_response, st.session_state.current_prompt)
            
            # Update the session state with the new prompt
            st.session_state.current_prompt = feedback_and_question  # Update the prompt
            
            st.rerun()  # Rerun to refresh the page
            
        except Exception as e:
            st.error(f"An error occurred while processing the response: {str(e)}")

# Optional: Add a reset button
if st.button("Reset Interview"):
    st.session_state.current_prompt = start_interview()  # Reset to the initial question
    st.session_state.user_response = ""  # Optionally clear the user response if desired
    st.experimental_rerun()

import streamlit as st
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

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
    st.session_state.current_prompt = "Tell me about yourself and why you are interested in this role."
if "user_response" not in st.session_state:
    st.session_state.user_response = ""

# App Title
st.title("Interactive Mock Interview")

# Display the current prompt/question with custom styling
st.markdown(
    f'<div class="interviewer-question">'
    f'<strong>Interviewer:</strong> {st.session_state.current_prompt}'
    f'</div>',
    unsafe_allow_html=True
)

# Input field for user's response
user_response = st.text_area("Your response:", value=st.session_state.user_response, height=150, key="response_area")

# Submit button with error handling
if st.button("Submit"):
    if not user_response.strip():
        st.warning("Please provide a response before submitting.")
    else:
        response_data = {
            "user_response": user_response
        }
        
        st.write("Sending request to Flask server...")  # Debug feedback
        
        try:
            # Send the user's response to the Flask backend
            res = requests.post("http://127.0.0.1:5001/quiz/response", json=response_data)
            st.write(f"Server response status: {res.status_code}")  # Debug feedback
            
            if res.status_code == 201:
                response_json = res.json()
                next_question = response_json.get("next_question")
                
                if not next_question:
                    st.error("No further questions available. The interview is complete!")
                else:
                    st.session_state.current_prompt = next_question  # Update the prompt
                    st.session_state.user_response = ""  # Clear the response area
                    st.rerun()  # Rerun to refresh the page
            else:
                st.error("Error processing response. Please check the server log for more information.")
                st.write(f"Response content: {res.text}")  # Print the response content for debugging
        except requests.exceptions.ConnectionError:
            st.error("Cannot connect to the server. Make sure it is running.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")

# Optional: Add a reset button
if st.button("Reset Interview"):
    try:
        requests.post("http://127.0.0.1:5001/quiz/reset")
        st.session_state.current_prompt = "Tell me about yourself and why you are interested in this role."
        st.session_state.user_response = ""
        st.rerun()
    except Exception as e:
        st.error(f"Error resetting interview: {str(e)}")

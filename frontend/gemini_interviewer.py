# Licensed under the Apache License, Version 2.0 (the "License");
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st  # For the front-end interface
import google.generativeai as genai  # Google Generative AI SDK
import os  # To retrieve the API key from environment variables

# Ensure that the API key is properly set
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    st.error("Missing API key! Set GOOGLE_API_KEY as an environment variable.")
else:
    genai.configure(api_key=GOOGLE_API_KEY)

# Define the Gemini AI model
model = genai.GenerativeModel('gemini-pro')

# Candidate details
age = 25
gender = "female"
location = "Tunisia"
current_job_type = "graduate student"
new_job_type = "software engineer"

# Function to initialize the first question
def start_interview():
    initial_question = "Tell me about yourself and why you are interested in this role."
    return initial_question

# Function to analyze the user's response and generate the next question
def analyze_response_and_prompt_next_question(user_response, previous_prompt):
    prompt = (
        f"**Interviewer:** {previous_prompt}\n\n"
        f"**Candidate:** \"{user_response}\"\n\n"
        f"You are a career coach role playing as interviewer with the user to improve their performance during interviews. "
        f"You are interviewing a {age}-year-old {gender} from {location} transitioning from {current_job_type} to {new_job_type}. "
        f"As the interviewer, provide positive feedback on the candidate's response. "
        f"Analyze the response for confidence and communication skills. "
        f"Suggest a more confident response using conversational language, similar to real-life interviews, with coaching statements for leadership and communication. "
        f"Use the job_type to suggest additional information the user could provide in their answer. "
        f"Ask the next question to explore soft skills like leadership, teamwork, and adaptability, but do not mention these skills directly in the question. "
    )

    # Call the Gemini model with the prompt
    response = model.generate_content(prompt)
    response_text = response.text

    # Extract the next question and feedback from the response
    interviewer_feedback_and_question = response_text.split("**Interviewer:**")[-1].strip()

    return interviewer_feedback_and_question

# Function to run the interview process with Streamlit
def interview_process():
    st.subheader("Interactive Mock Interview")
    current_prompt = start_interview()

    # Display the initial question
    st.markdown(f"**Interviewer:** {current_prompt}")

    # Input field for the user's response
    user_response = st.text_input("Your response:")

    # When the user submits their response
    if st.button("Submit"):
        # Analyze the response and get the next question
        gemini_response = analyze_response_and_prompt_next_question(user_response, current_prompt)

        # Display the feedback and next question
        st.markdown(f"**Interviewer:** {gemini_response}")

        # Update the prompt for the next iteration
        st.session_state.current_prompt = gemini_response.split('\n')[-1].strip()

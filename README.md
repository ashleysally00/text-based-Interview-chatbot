# Quick Start Guide

This chatbot app is designed to run on Streamlit and provides a text-based interview experience powered by the Gemini API. Each time you answer a question and submit, it generates a new question based on your previous answer. Currently, the text box does not clear when you move on to the next question, so you will see your previous response in the box and can type your new answer below it.

## Steps to Run, Modify, and Test Locally

1. **Clone or Download the Repository**
   * Clone this repo to your local environment or download it as a ZIP file.

2. **Set Up Environment Variables**
   * In the root project folder, create a `.env` file.
   * Add your Gemini API key and Google API key to the `.env` file in the following format:
     ```
     GEMINI_API_KEY="your_gemini_api_key_here"
     GOOGLE_API_KEY="your_google_api_key_here"
     ```

3. **Create and Activate a Virtual Environment**
   * In the root project folder, create a virtual environment:
     ```bash
     python3 -m venv venv
     ```
   * Activate the virtual environment:
     ```bash
     # On Unix/macOS
     source venv/bin/activate
     
     # On Windows
     .\venv\Scripts\activate
     ```

4. **Install Required Libraries**
   * Use `requirements.txt` to install the dependencies:
     ```bash
     pip install -r requirements.txt
     ```

5. **Run the Backend and Frontend**
   * Open a split terminal or two separate terminals:
     * **Backend**: In one terminal, navigate to the backend folder and start the Flask server:
       ```bash
       cd backend
       python3 server.py
       ```
     * **Frontend**: In the other terminal, navigate to the frontend folder and start the Streamlit app:
       ```bash
       cd frontend
       streamlit run app.py
       ```

6. **Access the App**
   * Once both servers are running, open `http://localhost:8501` in your browser to access the app.


# she-builds-ai-chatbot

Welcome to the Interactive Text-Based Interview Chatbot! This application uses the Gemini API to generate responses for interview questions in real-time.

## Live Demo

You can test the application using the following link: I have not added the link yet because need to deploy it from Github to Streamlit Cloud
[Interactive Chatbot Interface](http://localhost:8508) 


## Getting Started

Follow these instructions to set up the project locally.

### Prerequisites

Make sure you have Python installed (version 3.7 or higher). You can download Python from [python.org](https://www.python.org/downloads/).

### Installation

#### 1. Clone the Repository

To get a local copy of this project, you can either download it as a ZIP file or clone it using Git:

```bash
git clone https://github.com/ashleysally00/she-builds-ai-chatbot.git
```

#### 2. Create a Virtual Environment

Navigate to the project directory and create a virtual environment:

```bash
cd she-builds-ai-chatbot  # Change to your cloned repository directory
python -m venv venv       # Create a virtual environment named 'venv'
```

#### 3. Activate the Virtual Environment

**For macOS/Linux:**
```bash
source venv/bin/activate
```

**For Windows:**
```bash
venv\Scripts\activate
```

#### 4. Install Required Packages

To install the necessary packages, run the following command:

```bash
pip install -r requirements.txt
```

This command will read the `requirements.txt` file in this repository and install all listed dependencies.

### Setting Up Your API Key

To use the Gemini API, you need an API key. Follow these steps to obtain your key:

1. **Sign Up for the Gemini API**
   * Go to the Gemini API website (replace with the actual link) and sign up for an account if you don't already have one.

2. **Obtain Your API Key**
   * Once registered, navigate to your account settings or API section to find your API key.

3. **Create a `.env` File**
   * In the root directory of your project, create a file named `.env` and add your API key in the following format:
     ```plaintext
     GOOGLE_API_KEY=your_api_key_here
     ```
   * Replace `your_api_key_here` with your actual API key.

### Running the Application

To start the Streamlit app, use the following command:

```bash
streamlit run frontend/app.py
```

This will launch the app in your default web browser.

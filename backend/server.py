from flask import Flask, request, jsonify
import os
import json
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the API key with verification
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
print(f"API Key loaded: {'Yes' if GOOGLE_API_KEY else 'No'}")  # Debug API key status

if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)
else:
    print("WARNING: No Google API key found!")

# In-memory storage for interview context
interview_context = []

@app.route('/quiz/response', methods=['POST'])
def save_quiz_response():
    print("\n=== New Request Received ===")
    data = request.json
    user_response = data.get("user_response", "")
    
    # Add to context
    interview_context.append({
        "role": "candidate",
        "response": user_response
    })
    
    # Generate next question
    next_question = generate_next_question(interview_context)
    print(f"\nGenerated Next Question: {next_question}")  # Log the generated question
    
    # Prepare response
    response_data = {
        "message": "Response saved",
        "next_question": next_question,
        "context_length": len(interview_context)
    }
    print(f"\nSending Response: {json.dumps(response_data, indent=2)}")  # Log the response being sent
    
    return jsonify(response_data), 201
        
def generate_next_question(context):
    print("\n=== Generating Next Question ===")
    prompt = create_interview_prompt(context)
    print(f"\nUsing Prompt:\n{prompt}")
    
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    
    question = response.text.strip()
    question = question.replace("Interviewer:", "").strip()
    
    print(f"\nGenerated Raw Question: {question}")
    return question
        
def create_interview_prompt(context):
    prompt = [
        "You are a professional interviewer conducting a job interview.",
        "Based on the following conversation history, generate a relevant follow-up question.",
        "The question should be insightful and relate to the candidate's previous responses.\n"
    ]
    
    # Add conversation history
    for entry in context:
        if entry["role"] == "interviewer":
            prompt.append(f"Interviewer: {entry['question']}")
        else:
            prompt.append(f"Candidate: {entry['response']}")
    
    prompt.append("\nGenerate a specific, professional follow-up question that naturally builds on the conversation.")
    return "\n".join(prompt)

@app.route('/quiz/reset', methods=['POST'])
def reset_interview():
    print("\n=== Resetting Interview ===")
    global interview_context
    old_length = len(interview_context)
    interview_context = []
    print(f"Reset complete. Cleared {old_length} entries.")
    return jsonify({"message": "Interview reset successfully"}), 200

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "api_key_configured": bool(GOOGLE_API_KEY),
        "context_length": len(interview_context)
    }), 200

if __name__ == '__main__':
    print("\n=== Starting Interview Server ===")
    app.run(port=5001, debug=True)

# Path: backend/google/generativeai.py  
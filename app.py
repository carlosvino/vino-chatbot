from flask import Flask, request, jsonify
from flask_cors import CORS  # ✅ Import CORS to fix cross-origin issues
import openai
import os

app = Flask(__name__)
CORS(app)  # ✅ Enable CORS

# Load OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Vino Chatbot API is running!"})

@app.route("/chatbot", methods=["POST"])
def chatbot():
    try:
        user_input = request.json.get("message")
        if not user_input:
            return jsonify({"error": "No message provided"}), 400  # Return HTTP 400 if no input

        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an AI chatbot for Vino Design Build, helping users with remodeling, ADUs, and construction inquiries."},
                {"role": "user", "content": user_input}
            ]
        )

        # ✅ Fix: The new API structure requires indexing with dictionary keys
        chatbot_reply = response["choices"][0]["message"]["content"]

        return jsonify({"response": chatbot_reply})

    except Exception as e:  # ✅ Generic error handling for now
        return jsonify({"error": f"Server Error: {str(e)}"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

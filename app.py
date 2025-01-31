from flask import Flask, request, jsonify
from flask_cors import CORS  # ✅ Fixes cross-origin issues
import openai
import os

app = Flask(__name__)
CORS(app)  # ✅ Allow API to be accessed from your frontend

# ✅ Fix: Correct OpenAI Client Initialization
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Vino Chatbot API is running!"})

@app.route("/chatbot", methods=["POST"])
def chatbot():
    try:
        user_input = request.json.get("message")
        if not user_input:
            return jsonify({"error": "No message provided"}), 400  # ✅ Handles missing input

        # ✅ Fix: Use correct OpenAI API call
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an AI chatbot for Vino Design Build, helping users with remodeling, ADUs, and construction inquiries."},
                {"role": "user", "content": user_input}
            ]
        )

        # ✅ Fix: Correct indexing for chatbot response
        chatbot_reply = response.choices[0].message.content

        return jsonify({"response": chatbot_reply})

    except openai.OpenAIError as e:  # ✅ Proper error handling
        return jsonify({"error": f"OpenAI API Error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Server Error: {str(e)}"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

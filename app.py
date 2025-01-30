from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Load OpenAI API Key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chatbot", methods=["POST"])
def chatbot():
    user_input = request.json.get("message")

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an AI chatbot for Vino Design Build, helping users with remodeling, ADUs, and construction inquiries."},
            {"role": "user", "content": user_input}
        ]
    )

    return jsonify({"response": response["choices"][0]["message"]["content"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

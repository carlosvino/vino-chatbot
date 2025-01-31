import json
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)
CORS(app)

# ✅ Correct way to set OpenAI API key
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ✅ Load Google Sheets credentials from environment variable
creds_json = os.getenv("GOOGLE_CREDENTIALS")  # Load from Render env variable
creds_dict = json.loads(creds_json)  # Convert JSON string to dictionary
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
gs_client = gspread.authorize(creds)
sheet = gs_client.open("Vino Leads").sheet1  # Open the first sheet

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Vino Chatbot API is running!"})

@app.route("/chatbot", methods=["POST"])
def chatbot():
    try:
        user_input = request.json.get("message")
        user_email = request.json.get("email", "Not provided")  # Optional email input
        user_name = request.json.get("name", "Not provided")  # Optional name input

        if not user_input:
            return jsonify({"error": "No message provided"}), 400

        # ✅ Update to new OpenAI SDK syntax
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an AI chatbot for Vino Design Build, helping users with remodeling, ADUs, and construction inquiries."},
                {"role": "user", "content": user_input}
            ]
        )

        chatbot_reply = response.choices[0].message.content

        # ✅ Save the lead to Google Sheets
        sheet.append_row([user_name, user_email, user_input, chatbot_reply])

        return jsonify({"response": chatbot_reply})

    except openai.OpenAIError as e:
        return jsonify({"error": f"OpenAI API Error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Server Error: {str(e)}"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

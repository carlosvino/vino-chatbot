import json
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)
CORS(app)

# ✅ Correct OpenAI API Key
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ✅ Load Google Sheets credentials
creds_json = os.getenv("GOOGLE_CREDENTIALS")  # Load from Render env variable
creds_dict = json.loads(creds_json)  # Convert JSON string to dictionary
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file"
]
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
gs_client = gspread.authorize(creds)

# ✅ Debugging: Print available spreadsheets to log
try:
    spreadsheets = gs_client.openall()
    available_sheets = [s.title for s in spreadsheets]
    print(f"✅ Available Spreadsheets: {available_sheets}")  # Logs available sheets
    if "VinoBot Leads" not in available_sheets:
        print("❌ ERROR: 'VinoBot Leads' NOT FOUND. Check sharing settings.")
except Exception as e:
    print(f"❌ ERROR: Unable to list available spreadsheets: {e}")

# ✅ Try to open the sheet safely
try:
    sheet = gs_client.open("VinoBot Leads").sheet1  # Open the first sheet
    print("✅ Successfully connected to 'VinoBot Leads'")
except gspread.exceptions.SpreadsheetNotFound:
    print("❌ ERROR: Spreadsheet 'VinoBot Leads' NOT FOUND. Check service account access.")
    sheet = None  # Prevents app from crashing

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Vino Chatbot API is running!"})

@app.route("/chatbot", methods=["POST"])
def chatbot():
    try:
        user_input = request.json.get("message", "").strip().lower()
        user_email = request.json.get("email", "").strip()
        user_name = request.json.get("name", "").strip()

        if not user_input:
            return jsonify({"error": "No message provided"}), 400

        # ✅ Detect if user provided name & email, only ask if missing
        if not user_name or not user_email:
            return jsonify({"response": "Before we proceed, can you provide your **name** and **email**? This will help us assist you better!"})

        # ✅ Updated System Prompt to Ensure Lead Capture Happens Only Once
        system_prompt = (
            "You are an AI chatbot for Vino Design Build. "
            "Your primary goal is to collect the user's name, email, and project details "
            "BEFORE answering in full. If the user hasn't provided this info, ask for it first. "
            "If they have provided this info, proceed with answering their questions."
        )

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ]
        )

        chatbot_reply = response.choices[0].message.content

        # ✅ Save to Google Sheets if available
        if sheet:
            sheet.append_row([user_name, user_email, user_input, chatbot_reply])
            print(f"✅ Lead saved: {user_name}, {user_email}, {user_input}")
        else:
            print("❌ ERROR: Google Sheet not available. Lead not saved.")

        return jsonify({"response": chatbot_reply})

    except openai.OpenAIError as e:
        print(f"❌ OpenAI API Error: {e}")
        return jsonify({"error": f"OpenAI API Error: {str(e)}"}), 500
    except Exception as e:
        print(f"❌ Server Error: {e}")
        return jsonify({"error": f"Server Error: {str(e)}"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

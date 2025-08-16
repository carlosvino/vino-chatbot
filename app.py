import json
import os
import re  # ✅ Import regex for better email/name extraction
import uuid
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)
CORS(app)

# In-memory conversation store for advanced contextual chats
conversations = {}


@app.before_request
def log_request():
    """Log basic request information for debugging and analytics."""
    app.logger.info(
        f"{datetime.utcnow().isoformat()} | {request.remote_addr} | {request.method} {request.path}"
    )

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

# ✅ Regex for extracting name and email
EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
NAME_REGEX = r"^\s*([A-Za-z]+)\s"

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Vino Chatbot API is running!"})

@app.route("/chatbot", methods=["POST"])
def chatbot():
    try:
        user_input = request.json.get("message", "").strip()
        user_email = request.json.get("email", "").strip()
        user_name = request.json.get("name", "").strip()

        session_id = request.json.get("session_id") or user_email or str(uuid.uuid4())
        history = conversations.setdefault(session_id, [])

        # ✅ Extract email and name if they were included in the input message
        if not user_email:
            extracted_email = re.search(EMAIL_REGEX, user_input)
            if extracted_email:
                user_email = extracted_email.group(0)

        if not user_name:
            extracted_name = re.search(NAME_REGEX, user_input)
            if extracted_name:
                user_name = extracted_name.group(1)

        # ✅ Ask for missing info only if needed
        if not user_name or not user_email:
            return jsonify({"response": "Before we proceed, can you provide your **name** and **email**? Example: 'My name is John and my email is john@example.com'."})

        # ✅ Updated System Prompt to Ensure Lead Capture Happens Only Once
        system_prompt = (
            "You are an AI chatbot for Vino Design Build. "
            "Your primary goal is to collect the user's name, email, and project details "
            "BEFORE answering in full. If the user hasn't provided this info, ask for it first. "
            "If they have provided this info, proceed with answering their questions."
        )

        history.append({"role": "user", "content": user_input})
        messages = [{"role": "system", "content": system_prompt}] + history

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )

        chatbot_reply = response.choices[0].message.content
        history.append({"role": "assistant", "content": chatbot_reply})
        if len(history) > 10:
            conversations[session_id] = history[-10:]

        # ✅ Save to Google Sheets if available
        if sheet:
            sheet.append_row([user_name, user_email, user_input, chatbot_reply])
            print(f"✅ Lead saved: {user_name}, {user_email}, {user_input}")
        else:
            print("❌ ERROR: Google Sheet not available. Lead not saved.")

        return jsonify({"response": chatbot_reply, "session_id": session_id})

    except openai.OpenAIError as e:
        print(f"❌ OpenAI API Error: {e}")
        return jsonify({"error": f"OpenAI API Error: {str(e)}"}), 500
    except Exception as e:
        print(f"❌ Server Error: {e}")
        return jsonify({"error": f"Server Error: {str(e)}"}), 500

@app.route("/reset", methods=["POST"])
def reset_session():
    """Reset conversation history for a given session."""
    session_id = request.json.get("session_id")
    if session_id and session_id in conversations:
        del conversations[session_id]
        return jsonify({"status": "reset"})
    return jsonify({"error": "session_id not found"}), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

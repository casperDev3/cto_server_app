import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

CORS(app, origins=["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:63342"])

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

@app.route('/submit_form', methods=['POST'])
def submit_form():
    data = request.get_json()
    print(data)

    full_name = data.get("fullName")
    phone_number = data.get("phoneNumber")
    email = data.get("email")
    telegram_user = data.get("telegramUser", "Не вказано")

    message = (f"📩 Нова заявка на СТО\n\n"
               f"👤 Ім'я: {full_name}\n"
               f"📞 Телефон: {phone_number}\n"
               f"📧 Email: {email}\n"
               f"💬 Telegram: {telegram_user}")

    response = requests.post(TELEGRAM_API_URL, json={
        "chat_id": ADMIN_CHAT_ID,
        "text": message
    })

    if response.status_code == 200:
        return jsonify({"status": "success", "message": "Заявка надіслана!"})
    else:
        return jsonify({"status": "error", "message": "Помилка при надсиланні"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)

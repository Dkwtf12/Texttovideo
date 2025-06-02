#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "19977673"))
API_HASH = environ.get("API_HASH", "f75386c7aab88e2ad9b5de220fc0ceb4")
BOT_TOKEN = environ.get("BOT_TOKEN", "5151746178:AAGGFu7WFHC0J9g-b7eUIc5uzNUBfyxsEtk")
OWNER = int(environ.get("OWNER", "1568895149"))
CREDIT = "𝄟⃝‌🐬🇳‌ɪᴋʜɪʟ𝄟⃝🐬"
AUTH_USER = os.environ.get('AUTH_USERS', '8024721215').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "28460032"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "1457c3ba64719a1e442aae67217b67c2")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8150025209:AAHstLep9sQePj2X0YvitaXfgmz8EvKsGY0")

OWNER_ID = int(os.environ.get("OWNER_ID", "7575753569"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "7575753569").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://wadiro6523:08AwfhhKRdQaS1i6@cluster0.krzxuop.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002798076483"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "-1002798076483")  # Optional here you'll get all logs

import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))
DATA_FILE = "data/projects.json"
BASE_DIR = os.getenv("BASE_DIR", ".")
AI_MODEL = os.getenv("AI_MODEL", "claude-sonnet-4.6")

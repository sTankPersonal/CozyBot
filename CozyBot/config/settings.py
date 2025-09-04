import os
from dotenv import load_dotenv

load_dotenv()

# Bot configuration settings

# Discord bot token (keep this secret!)
TOKEN = os.getenv("TOKEN")

# Command prefix for your bot
PREFIX = os.getenv("PREFIX", "!")  # Default to "!" if not set
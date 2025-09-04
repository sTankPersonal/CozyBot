import os

# Bot configuration settings

# Discord bot token (keep this secret!)
TOKEN = os.getenv("BOT_TOKEN")

# Command prefix for your bot
PREFIX = os.getenv("PREFIX", "!")  # Default to "!" if not set
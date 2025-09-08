import os

# Bot configuration settings

# Your bot token - https://discord.com/developers/docs/intro
# Required environment variable 
TOKEN = os.getenv("BOT_TOKEN")

# Database connection string - Any SQLAlchemy supported database - https://docs.sqlalchemy.org/en/20/orm/quickstart.html
# Required environment variable
DB_CONNECTION_STRING = os.getenv("DB_CONNECTION_STRING")

# Optional environment variable for command prefix
PREFIX = os.getenv("PREFIX", "!cozy") 

# Optional environment variable for bot name displayed in embeds
BOT_NAME = os.getenv("BOT_NAME", "CozyBot")

# Optional environment variable for footer text in embeds
FOOTER = os.getenv("FOOTER", "CozyBot - Developed By Sean T 2025 - https://github.com/sTankPersonal/CozyBot")
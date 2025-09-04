import discord
from discord.ext import commands
import asyncio
import logging

from config import settings
from utils.builders.intent_builder import IntentBuilder

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

intents = (
    IntentBuilder()
    .enable_default()
    .members(True)
    .message_content(True)
    .build()
)

bot = commands.Bot(command_prefix=settings.PREFIX, intents=intents)

async def main():
    # Load extensions asynchronously
    await bot.load_extension('cogs.moderation.members')
    await bot.load_extension('cogs.moderation.messages')
    # Start the bot
    await bot.start(settings.TOKEN)
    logging.info("Bot has started.")



if __name__ == "__main__":
    asyncio.run(main())
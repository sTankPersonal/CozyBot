from discord.ext import commands
import discord
import asyncio
import logging

from Config import Settings
from Domain.Services.ValidateSettingsService import ValidateSettingsService 

# Validate settings at startup
ValidateSettingsService.validate(Settings.__dict__)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

# Directly configure intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=Settings.PREFIX, intents=intents)

async def main():
    # Load extensions asynchronously
    await bot.load_extension('Interface.EventHandlers.MemberEvents')
    await bot.load_extension('Interface.EventHandlers.MessageEvents')
    await bot.load_extension('Interface.EventHandlers.GuildEvents')
    await bot.load_extension('Interface.EventHandlers.ModerationEvents')
    # Start the bot
    await bot.start(Settings.TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
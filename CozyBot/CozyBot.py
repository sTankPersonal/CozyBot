import discord
from discord.ext import commands    

from config import settings
from utils.builders.intent_builder import IntentBuilder

intents = (
    IntentBuilder()
    .enable_default()
    .members(True)
    .message_content(True)
    .build()
)
bot = commands.Bot(command_prefix=settings.PREFIX, intents=intents)

bot.load_extension('cogs.moderation')
bot.load_extension('cogs.fun')

bot.run(settings.TOKEN)
import discord
from discord.ext import commands    

from config import settings

bot = commands.Bot(command_prefix=settings.PREFIX)

bot.load_extension('cogs.moderation')
bot.load_extension('cogs.fun')

bot.run(settings.TOKEN)
from discord.ext import commands

class Messages(commands.Cog):
    """Cog for moderation-related message commands."""

    def __init__(self, bot):
        self.bot = bot

# Required async setup function for Discord.py v2.x+
async def setup(bot):
    await bot.add_cog(Messages(bot))
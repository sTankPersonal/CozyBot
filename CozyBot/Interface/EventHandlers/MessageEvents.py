from discord.ext import commands

class MessageEvents(commands.Cog):
    """Cog for moderation-related message commands."""

    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(MessageEvents(bot))
from discord.ext import commands

class ModerationEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        prefix = self.bot.command_prefix

        print(f"Bot is ready! Command prefix: {prefix}")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(f"Command error: {error}")

async def setup(bot):
    await bot.add_cog(ModerationEvents(bot))
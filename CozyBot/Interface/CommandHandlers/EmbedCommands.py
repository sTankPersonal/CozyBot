from discord.ext import commands
from Infrastructure.Repositories.ServerRepository import ServerRepository
from Domain.Entities.Server import Server
from Domain.Services.DiscordEmbedService import DiscordEmbedService

class GuildEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # WIP
    # @commands.command(name="create_embed")
    # @commands.has_permissions(administrator=True)
    # async def create_embed(self, ctx, title: str, description: str):
    #     embed = DiscordEmbedService().create_generic_embed(
    #         title=title,
    #         description=description,
    #         color=0x00FF00
    #     )
    #     await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(GuildEvents(bot))
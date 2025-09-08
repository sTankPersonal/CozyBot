from discord.ext import commands
from Infrastructure.Repositories.ServerRepository import ServerRepository
from Domain.Entities.Server import Server
from Domain.Services.DiscordEmbedService import DiscordEmbedService

class GuildEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        if not ServerRepository().get_by_discord_id(str(guild.id)):
            new_server = Server(discord_id=str(guild.id))
            ServerRepository().add(new_server)
        embed = DiscordEmbedService().create_generic_embed(
            title="Thanks for adding me to your server!",
            description="I'm excited to be here! Usage can be found at https://github.com/sTankPersonal/CozyBot",
            color=0x00FF00
        )
        await guild.system_channel.send(embed=embed)

    @commands.command(name="testguild")
    @commands.has_permissions(administrator=True)
    async def test_guild(self, ctx):
        """Manually test the on_guild_join logic."""
        print("Testing guild join logic...")
        guild = ctx.guild
        if not ServerRepository().get_by_discord_id(str(guild.id)):
            new_server = Server(discord_id=str(guild.id))
            ServerRepository().add(new_server)
        embed = DiscordEmbedService().create_generic_embed(
            title="Thanks for adding me to your server!",
            description="I'm excited to be here! Usage can be found at https://github.com/sTankPersonal/CozyBot",
            color=0x00FF00
        )
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(f"Command error: {error}")
        embed = DiscordEmbedService().create_generic_embed(
            title="An error occurred",
            description=str(error),
            color=0xFF0000
        )
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(GuildEvents(bot))

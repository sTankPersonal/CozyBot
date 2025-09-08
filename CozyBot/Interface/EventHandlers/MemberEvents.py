from discord import guild
from discord.ext import commands
import random
from Infrastructure.Repositories.MessageRepository import MessageRepository
from Domain.Enums.MessageType import MessageType
from Domain.Services.DiscordEmbedService import DiscordEmbedService


class MemberEvents(commands.Cog):
    """Handles member join and leave events."""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild_id = member.guild.id
        channel = member.guild.system_channel
        messages_list = MessageRepository().get_all(
            server_id=guild_id, messageType=MessageType.ON_MEMBER_JOIN)
        
        embed = None
        if len(messages_list) > 0:
            embed = DiscordEmbedService.create_embed(random.choice(messages_list))
        else:
            embed = DiscordEmbedService.create_error_embed(404, "No welcome message could be found.")
        
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        guild_id = member.guild.id
        channel = member.guild.system_channel
        messages_list = MessageRepository().get_all(
            server_id=guild_id, messageType=MessageType.ON_MEMBER_LEAVE)
        
        embed = None
        if len(messages_list) > 0:
            embed = DiscordEmbedService.create_embed(random.choice(messages_list))
        else:
            embed = DiscordEmbedService.create_error_embed(404, "No farewell message could be found.")
        
        await channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(MemberEvents(bot))
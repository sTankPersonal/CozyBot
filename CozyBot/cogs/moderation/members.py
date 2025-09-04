import discord
from discord.ext import commands
from datetime import datetime
from utils.builders.embed_builder import EmbedBuilder
from cogs.moderation import messages

class MemberEvents(commands.Cog):
    """Handles member join and leave events."""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel:
            msg = messages.JOIN_MESSAGE
            embed_builder = EmbedBuilder(
                title=msg["title"],
                description=msg["description"].format(
                    mention=member.mention,
                    server=member.guild.name
                ),
                color=msg["color"]
            )
            # Author
            author = msg.get("author")
            if author:
                icon_url = author.get("icon_url") or self.bot.user.avatar.url
                embed_builder.set_author(name=author["name"], icon_url=icon_url)
            # Thumbnail
            thumbnail = msg.get("thumbnail") or member.avatar.url
            if thumbnail:
                embed_builder.set_thumbnail(url=thumbnail)
            # Image
            image = msg.get("image")
            if image:
                embed_builder.set_image(url=image)
            # Fields
            for field in msg.get("fields", []):
                embed_builder.add_field(**field)
            # Footer
            footer = msg.get("footer")
            if footer:
                embed_builder.set_footer(text=footer["text"], icon_url=footer.get("icon_url"))
            # Timestamp
            embed_builder.set_timestamp(datetime.utcnow())
            await channel.send(embed=embed_builder.build())

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = member.guild.system_channel
        if channel:
            msg = messages.LEAVE_MESSAGE
            embed_builder = EmbedBuilder(
                title=msg["title"],
                description=msg["description"].format(mention=member.mention),
                color=msg["color"]
            )
            footer = msg.get("footer")
            if footer:
                embed_builder.set_footer(text=footer["text"], icon_url=footer.get("icon_url"))
            embed_builder.set_timestamp(datetime.utcnow())
            await channel.send(embed=embed_builder.build())

async def setup(bot):
    await bot.add_cog(MemberEvents(bot))
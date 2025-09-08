from Domain.Entities.Message import Message
import discord
from Config.Settings import BOT_NAME, FOOTER

class DiscordEmbedService:
    def create_embed(self, message: Message) -> discord.Embed:
        embed = discord.Embed(
            title=message.title,
            description=message.description,
            color=message.color if message.color else 0x000000,
            url=message.title_url if message.title_url else discord.Embed.Empty
        )
        if message.thumbnail_url:
            embed.set_thumbnail(url=message.thumbnail_url)
        if message.image_url:
            embed.set_image(url=message.image_url)
        for field in message.fields:
            embed.add_field(
                name=field.name,
                value=field.value,
                inline=field.inline
            )
        embed.set_author(name=BOT_NAME)
        embed.set_footer(text=FOOTER)
        return embed

    def create_error_embed(self, error_code: str, error_string: str) -> discord.Embed:
        embed = discord.Embed(
            title=f"Error {error_code}",
            description=error_string,
            color=0xE74C3C 
        )
        embed.set_author(name=BOT_NAME)
        embed.set_footer(text=FOOTER)
        return embed

    def create_generic_embed(self, title: str, description: str, color: int) -> discord.Embed:
        embed = discord.Embed(
            title=title,
            description=description,
            color=color
        )
        embed.set_author(name=BOT_NAME)
        embed.set_footer(text=FOOTER)
        return embed

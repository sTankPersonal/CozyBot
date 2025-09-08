# import discord
# from typing import Optional, Union
# from datetime import datetime

# class EmbedBuilder:
#     def __init__(
#         self,
#         title: Optional[str] = None,
#         description: Optional[str] = None,
#         color: Optional[Union[discord.Color, int]] = None,
#         type_: str = "rich",
#         url: Optional[str] = None,
#         timestamp: Optional[datetime] = None
#     ):
#         self.embed = discord.Embed(
#             title=title,
#             description=description,
#             color=color,
#             type=type_,
#             url=url,
#             timestamp=timestamp
#         )

#     def set_author(self, name: str, url: Optional[str] = None, icon_url: Optional[str] = None):
#         self.embed.set_author(name=name, url=url, icon_url=icon_url)
#         return self

#     def remove_author(self):
#         self.embed.remove_author()
#         return self

#     def set_footer(self, text: Optional[str] = None, icon_url: Optional[str] = None):
#         self.embed.set_footer(text=text, icon_url=icon_url)
#         return self

#     def remove_footer(self):
#         self.embed.remove_footer()
#         return self

#     def set_thumbnail(self, url: str):
#         self.embed.set_thumbnail(url=url)
#         return self

#     def set_image(self, url: str):
#         self.embed.set_image(url=url)
#         return self

#     def add_field(self, name: str, value: str, inline: bool = False):
#         self.embed.add_field(name=name, value=value, inline=inline)
#         return self

#     def insert_field_at(self, index: int, name: str, value: str, inline: bool = False):
#         self.embed.insert_field_at(index, name=name, value=value, inline=inline)
#         return self

#     def set_field_at(self, index: int, name: str, value: str, inline: bool = False):
#         self.embed.set_field_at(index, name=name, value=value, inline=inline)
#         return self

#     def remove_field(self, index: int):
#         self.embed.remove_field(index)
#         return self

#     def clear_fields(self):
#         self.embed.clear_fields()
#         return self

#     def set_timestamp(self, timestamp: datetime):
#         self.embed.timestamp = timestamp
#         return self

#     def set_url(self, url: str):
#         self.embed.url = url
#         return self

#     def set_title(self, title: str):
#         self.embed.title = title
#         return self

#     def set_description(self, description: str):
#         self.embed.description = description
#         return self

#     def set_color(self, color: Union[discord.Color, int]):
#         self.embed.color = color
#         return self

#     def build(self):
#         return self.embed
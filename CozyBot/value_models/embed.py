from typing import Optional, List, Dict, Any, Union
from datetime import datetime

class Embed:
    def __init__(
        self,
        title: Optional[str] = None,
        description: Optional[str] = None,
        color: Optional[Union[int, str]] = None,
        type_: str = "rich",
        url: Optional[str] = None,
        timestamp: Optional[datetime] = None,
        author: Optional[Dict[str, Any]] = None,
        footer: Optional[Dict[str, Any]] = None,
        thumbnail_url: Optional[str] = None,
        image_url: Optional[str] = None,
        fields: Optional[List[Dict[str, Any]]] = None
    ):
        self.title = title
        self.description = description
        self.color = color
        self.type_ = type_
        self.url = url
        self.timestamp = timestamp
        self.author = author
        self.footer = footer
        self.thumbnail_url = thumbnail_url
        self.image_url = image_url
        self.fields = fields if fields is not None else []

    def __composite_values__(self):
        return (
            self.title,
            self.description,
            self.color,
            self.type_,
            self.url,
            self.timestamp,
            self.author,
            self.footer,
            self.thumbnail_url,
            self.image_url,
            tuple((f['name'], f['value'], f.get('inline', False)) for f in self.fields)
        )

    def __repr__(self):
        return (
            f"Embed(title={self.title!r}, description={self.description!r}, "
            f"color={self.color!r}, type_={self.type_!r}, url={self.url!r}, "
            f"timestamp={self.timestamp!r}, author={self.author!r}, "
            f"footer={self.footer!r}, thumbnail_url={self.thumbnail_url!r}, "
            f"image_url={self.image_url!r}, fields={self.fields!r})"
        )

    def __eq__(self, other):
        if not isinstance(other, Embed):
            return False
        return self.__composite_values__() == other.__composite_values__()
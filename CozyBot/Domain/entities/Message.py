from sqlalchemy import ForeignKey, Integer, String, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from Domain.Entities.AbstractBase import Base
from Domain.Enums.MessageType import MessageType
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Domain.Entities.Server import Server
    from Domain.Entities.EmbedField import EmbedField


class Message(Base):
    __tablename__ = 'messages'

    id: Mapped[int] = mapped_column(primary_key=True)
    server_id: Mapped[int] = mapped_column(ForeignKey("servers.id"))
    server: Mapped["Server"] = relationship("Server", back_populates="messages")

    message_type: Mapped[MessageType] = mapped_column(Enum(MessageType), nullable=False)
    title: Mapped[str] = mapped_column(String(256))
    description: Mapped[str] = mapped_column(String(2048))
    color: Mapped[int] = mapped_column(Integer)
    title_url: Mapped[str] = mapped_column(String(2048))
    thumbnail_url: Mapped[str] = mapped_column(String(2048))
    image_url: Mapped[str] = mapped_column(String(2048))

    fields: Mapped[list["EmbedField"]] = relationship("EmbedField", back_populates="message", cascade="all, delete-orphan")
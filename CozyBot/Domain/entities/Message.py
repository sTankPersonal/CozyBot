from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from Domain.Entities.AbstractBase import Base
from Domain.Entities.EmbedField import EmbedField
from Domain.Enums.MessageType import MessageType
from Domain.Entities.Server import Server



class Message(Base):
    __tablename__ = 'messages'

    #PK
    id: Mapped[int] = mapped_column(primary_key=True)
    #FK
    server_id: Mapped[int] = mapped_column(ForeignKey("server.id"))
    server: Mapped["Server"] = relationship(back_populates="messages")

    message_type: Mapped[MessageType] = mapped_column(MessageType, nullable=False)

    title: Mapped[str] = mapped_column(String(256))
    description: Mapped[str] = mapped_column(String(2048))
    color: Mapped[int] = mapped_column(Integer)
    title_url: Mapped[str] = mapped_column(String(2048))
    thumbnail_url: Mapped[str] = mapped_column(String(2048))
    image_url: Mapped[str] = mapped_column(String(2048))

    fields: Mapped[list["EmbedField"]] = relationship(back_populates="message", cascade="all, delete-orphan")
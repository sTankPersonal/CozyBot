from typing import List
from sqlalchemy import String
from sqlalchemy.orm import  Mapped, mapped_column, relationship

from Domain.Entities.Message import Message
from Domain.Entities.AbstractBase import Base


class Server(Base):
    __tablename__ = 'servers'

    id: Mapped[int] = mapped_column(primary_key=True)
    discord_id: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)

    messages: Mapped[List["Message"]] = relationship("Message", back_populates="server", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Server(id={self.id!r}, discord_id={self.discord_id!r})"



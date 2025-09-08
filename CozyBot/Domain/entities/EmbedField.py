from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from Domain.Entities.AbstractBase import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Domain.Entities.Message import Message

class EmbedField(Base):
    __tablename__ = 'embed_fields'

    #PK
    id: Mapped[int] = mapped_column(primary_key=True)

    #FK
    message_id: Mapped[int] = mapped_column(ForeignKey("messages.id"))
    message: Mapped["Message"] = relationship("Message", back_populates="fields")

    name: Mapped[str] = mapped_column(String(256))
    value: Mapped[str] = mapped_column(String(1024))
    inline: Mapped[bool] = mapped_column(default=False)   

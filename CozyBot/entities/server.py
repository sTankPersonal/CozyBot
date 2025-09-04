from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, composite

class Base(DeclarativeBase):
    pass

class ServerDetails:
    def __init__(self, server_name: str):
        self.server_name = server_name

    def __composite_values__(self):
        return (self.server_name,)

    def __repr__(self):
        return f"ServerDetails(server_name={self.server_name!r})"

    def __eq__(self, other):
        if isinstance(other, ServerDetails):
            return self.server_name == other.server_name
        return False

class Server(Base):
    __tablename__ = 'servers'

    id: Mapped[int] = mapped_column(primary_key=True)
    discord_id: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    
    server_name: Mapped[str] = mapped_column(String(100), nullable=False)

    details: Mapped[ServerDetails] = composite(ServerDetails, server_name)



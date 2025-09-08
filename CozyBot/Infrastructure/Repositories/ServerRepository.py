from Domain.Entities.Server import Server
from Infrastructure.Data.AppDbEngine import AppDbEngine

class ServerRepository:
    def __init__(self):
        self.db_engine = AppDbEngine()

    def get_all(self):
        with self.db_engine.session_scope() as session:
            return session.query(Server).all()

    def get(self, server_id):
        with self.db_engine.session_scope() as session:
            return session.query(Server).get(server_id)

    def add(self, server: Server):
        with self.db_engine.session_scope() as session:
            session.add(server)

    def update(self, server: Server):
        with self.db_engine.session_scope() as session:
            session.merge(server)

    def delete(self, server_id):
        with self.db_engine.session_scope() as session:
            server = session.query(Server).get(server_id)
            if server:
                session.delete(server)
from Infrastructure.Data.AppDbEngine import AppDbEngine
from Domain.Entities.Message import Message

class MessageRepository:
    def __init__(self, connection_string):
        self.db_engine = AppDbEngine(connection_string)

    def get_all(self):
        with self.db_engine.session_scope() as session:
            return session.query(Message).all()

    def get(self, message_id):
        with self.db_engine.session_scope() as session:
            return session.query(Message).get(message_id)

    def add(self, message: Message):
        with self.db_engine.session_scope() as session:
            session.add(message)

    def update(self, message: Message):
        with self.db_engine.session_scope() as session:
            session.merge(message)

    def delete(self, message_id):
        with self.db_engine.session_scope() as session:
            message = session.query(Message).get(message_id)
            if message:
                session.delete(message)
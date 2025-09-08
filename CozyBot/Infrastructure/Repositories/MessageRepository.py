from Infrastructure.Data.AppDbEngine import AppDbEngine
from Domain.Entities.Message import Message

class MessageRepository:
    def __init__(self):
        self.db_engine = AppDbEngine()

    def get_all(self, server_id = None, messageType = None):
        with self.db_engine.session_scope() as session:
            query = session.query(Message)
            if server_id is not None:
                query = query.filter(Message.server_id == server_id)
            if messageType is not None:
                query = query.filter(Message.message_type == messageType)
            return query.all()

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


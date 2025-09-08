from Infrastructure.Data.AppDbEngine import AppDbEngine
from Domain.Entities.EmbedField import EmbedField


class EmbedFieldRepository:
    def __init__(self):
        self.db_engine = AppDbEngine()
    def get_all(self):
        with self.db_engine.session_scope() as session:
            return session.query(EmbedField).all()
    def get(self, embed_field_id):
        with self.db_engine.session_scope() as session:
            return session.query(EmbedField).get(embed_field_id)
    def add(self, embed_field: EmbedField):
        with self.db_engine.session_scope() as session:
            session.add(embed_field)
    def update(self, embed_field: EmbedField):
        with self.db_engine.session_scope() as session:
            session.merge(embed_field)
    def delete(self, embed_field_id):
        with self.db_engine.session_scope() as session:
            embed_field = session.query(EmbedField).get(embed_field_id)
            if embed_field:
                session.delete(embed_field)
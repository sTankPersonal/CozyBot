from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# Singleton Service for Database Engine and Session Management
class AppDbEngine:
    _instance = None

    def __new__(cls, connection_string: str):
        if cls._instance is None:
            cls._instance = super(AppDbEngine, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, connection_string: str):
        if self._initialized:
            return
        self.engine = create_engine(connection_string, echo=True)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self._initialized = True

    @contextmanager
    def session_scope(self):
        session = self.SessionLocal()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
import os
import re

from driver.veez import user as app
from sqlalchemy import create_engine
from config import DATABASE_URL as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

if db and db.startswith("postgres://"):
    app = db.replace("postgres://", "postgresql://", 1)

BASE = declarative_base()

def start() -> scoped_session:
    engine = create_engine(app)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))

SESSION = start()
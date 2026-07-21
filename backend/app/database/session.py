print("=== session.py started ===")

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

print("=== sqlalchemy imported ===")

from app.core.config import DATABASE_URL

print("DATABASE_URL =", DATABASE_URL)

engine = create_engine(DATABASE_URL)

print("=== engine created ===")

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

print("=== SessionLocal created ===")
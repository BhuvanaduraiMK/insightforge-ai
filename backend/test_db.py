print("=== test_db.py started ===")

from app.database.session import engine

print("=== engine imported ===")

try:
    print("=== trying to connect ===")
    connection = engine.connect()
    print("✅ Database connected successfully!")
    connection.close()
    print("=== connection closed ===")
except Exception as e:
    print("❌ Database connection failed!")
    print(e)
from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5433/orders"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

try:
    conn = engine.connect()
    print("Connection successful!")
    conn.close()
except Exception as e:
    print("Connection failed:", e)

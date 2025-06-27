import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from connection import engine
from sqlalchemy import text

def test_connection():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version();"))
            version = result.fetchone()
            print("✅ Connected successfully!")
            print("PostgreSQL version:", version[0])
    except Exception as e:
        print("❌ Connection failed:")
        print(e)

if __name__ == "__main__":
    test_connection()

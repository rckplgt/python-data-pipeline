import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
from config.settings import DATA_SOURCE
from db.connection import engine
from sqlalchemy import text
from config.settings import DATABASE_URL

#def extract_data():
 #   print(f"Extracting data from {DATA_SOURCE}")
  #  return pd.read_csv(DATA_SOURCE)

def extract_from_database(query: str):
    print("Querying database...")
    #engine = create_engine(DATABASE_URL)
    return pd.read_sql_query(query, engine)

print(extract_from_database('SELECT * FROM USERS'))
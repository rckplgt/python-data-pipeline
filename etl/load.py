from db.connection import engine
import pandas as pd

def load_data(df: pd.DataFrame, table_name="my_table"):
    print(f"Loading data into {table_name} table...")
    df.to_sql(table_name, engine, if_exists='replace', index=False)
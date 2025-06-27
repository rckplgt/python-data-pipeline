def transform_data(df):
    print("Transforming data...")
    df = df.dropna()
    df.columns = [col.lower().strip() for col in df.columns]
    return df
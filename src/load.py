import pandas as pd
import os
from sqlalchemy import create_engine, text, inspect
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(
    f"postgresql+psycopg2://"
    f"{os.getenv('db_user')}:{os.getenv('db_password')}"
    f"@{os.getenv('db_host')}:{os.getenv('db_port')}"
    f"/{os.getenv('db_name')}"
)

df = pd.read_csv("data/processed/cloud_dataset__cleaned.csv")

# Check whether cloud_data already exists
inspector = inspect(engine)

if inspector.has_table("cloud_data"):
    # Remove old data without dropping the table
    with engine.begin() as conn:
        conn.execute(text("DELETE FROM cloud_data"))

# Load fresh data
df.to_sql(
    "cloud_data",
    engine,
    if_exists="append",
    index=False
)

print("data uploaded successfully")
import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
conn=psycopg2.connect(
    host=os.getenv("db_host"),
    port=os.getenv("db_port"),
    database=os.getenv("db_name"),
    user=os.getenv("db_user"),
    password=os.getenv("db_password")
)

print("connected successfully!")
conn.close()
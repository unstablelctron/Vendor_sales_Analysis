import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

# Create SQLite database engine
engine = create_engine("sqlite:///inventory.db")


def ingest_db(df, table_name, engine):
    """
    Loads a pandas DataFrame into the database as a table.
    Replaces the table if it already exists.
    """
    df.to_sql(
        table_name,
        con=engine,
        if_exists="replace",
        index=False
    )


def load_raw_data():
    """
    Reads all CSV files from the current directory
    and ingests them into the database with logging.
    """
    start = time.time()

    for file in os.listdir():
        if file.endswith(".csv"):
            df = pd.read_csv(file)
            table_name = file.replace(".csv", "").lower()

            logging.info(f"Ingesting {file} into database")
            ingest_db(df, table_name, engine)

    end = time.time()
    total_time = (end - start) / 60

    logging.info("Ingestion Completed")
    logging.info(f"Total time taken: {total_time:.2f} minutes")


if __name__ == "__main__":
    """
    Entry point of the script.
    Triggers the raw data ingestion process.
    """
    load_raw_data()

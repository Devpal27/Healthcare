import pandas as pd
import numpy as np
import os
from sqlalchemy import create_engine
import logging
import time
import os

os.makedirs("logs", exist_ok=True)
engine = create_engine('sqlite:///myhealthcare.db')
logging.basicConfig(
    filename="logs/myhealthcare.logs",
    level=logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    filemode = "a"
)
def load_raw_data():
    start = time.time()
    for file in os.listdir('dataset'):
        if file.endswith('.csv'):
            df = pd.read_csv(f'dataset/{file}')
            print(df.shape)
            logging.info(f'ingesting {file} in datebase')
            ingest_db(df,file[:-4],engine)
            end = time.time()
            total_time = (end - start) / 60
            logging.info(f'Total time taken to ingest {file} is {total_time} minutes')
            logging.info('------------------------------------------------Ingestion completed--------------------------------------------------')
def ingest_db(df,table_name,engine):
    df.to_sql(table_name, con = engine, if_exists='replace', index=False)
if __name__ == "__main__":
    load_raw_data()


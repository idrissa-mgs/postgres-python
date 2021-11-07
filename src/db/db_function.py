import sys
import os

import psycopg2
from sqlalchemy import create_engine
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import logging

from configparser import ConfigParser


def db_connect():
    conn = None
    try: 
        conn = psycopg2.connect(
            host="localhost",
            database=os.environ["DB_NAME"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"]
        )
        logging.info("CONNECTION TO THE DATABASE SUCCESS")
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(f'{error}')
    with open("cred.txt", "w") as f:
        f.write(os.environ["DB_NAME"])
    return conn


def load_data():
    pass

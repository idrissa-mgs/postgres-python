import os
import pandas as pd
import numpy as np
from datetime import datetime
from dateutil.parser import parse
import click
from sqlalchemy import create_engine



from db.db_function import  db_connect, read_sql

connect_alchemy = f"postgresql+psycopg2://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{'pg_db'}/{os.environ['DB_NAME']}"
engine = create_engine(connect_alchemy)
def is_date(string_date, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try: 
        parse(string_date, fuzzy=fuzzy)
        click.echo(string_date)
        return True

    except ValueError:
        click.echo("This is not a valid date please retry with a valid one")
        return False

click.command()
@click.option('--start-date', help='Start Date for stats')
@click.option('--end-date',default=None ,help='End Date for stats')
def get_stats(start_date, end_date):
    conn = db_connect()
    if is_date(start_date):
        stats_sql = read_sql("src/db/stats.sql")
        if end_date == None:
            query_part = f"= {start_date} GROUP BY 1,2 ORDER BY money_spent;"
            stats_date = start_date
        elif is_date(end_date):
            query_part = f"BETWEEN {start_date} and {end_date} GROUP BY 1,2 ORDER BY money_spent;" 
            stats_date = f'[{start_date}, {end_date}]'
    query = stats_sql.replace("stats_date", f"{stats_sql}") + query_part
    stats_df = pd.read_sql(query,con=conn)
    click.echo(f"{stats_df}")
    return stats_sql


if __name__ == "__main__":
    get_stats()



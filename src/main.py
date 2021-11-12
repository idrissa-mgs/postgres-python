import os
from click.utils import echo
import pandas as pd
import numpy as np
from datetime import datetime
from dateutil.parser import parse
import click
from sqlalchemy import create_engine



from db.db_function import  db_connect, read_sql, db_params

connect_alchemy = f"postgresql+psycopg2://{db_params['user']}:{db_params['password']}@{db_params['host']}/{db_params['database']}"
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

@click.command()
@click.option('--start-date', help='Start Date for stats')
@click.option('--end-date',default=None ,help='End Date for stats')
def get_stats(start_date, end_date):
    conn = db_connect()
    if is_date(start_date):
        stats_date = start_date
        stats_sql = read_sql("src/db/stats.sql")
        if end_date == None:
            query_part = f"='{start_date}' GROUP BY 1,2 ORDER BY money_spent DESC;"
        elif is_date(end_date):
            if parse(start_date) <= parse(end_date):
                query_part = f"BETWEEN '{start_date}' AND '{end_date}' GROUP BY 1,2 ORDER BY money_spent DESC;" 
                stats_date = f'({start_date}, {end_date})'
            else:
                click.echo("Start date must be sonner than  end date, Try again")
                return None
    query = stats_sql.replace("stats_date", f'{stats_date}') + query_part

    click.echo(query)
    stats_df = pd.read_sql(query,con=conn)
    click.echo(f"{stats_df}")
    return stats_sql


if __name__ == "__main__":
    get_stats()



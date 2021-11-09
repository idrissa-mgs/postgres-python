from click.utils import echo
import pandas as pd
import numpy as np
from datetime import datetime
from dateutil.parser import parse
import click



from db.db_function import  db_connect


@click.command()
@click.option('--string-date', help='date in string format')
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




players = {"MJ":["Michael Jordan", 49, "Chicago Bulls", "american"],
            "CR7": ["Cristiano Ronaldo", 35, "Manchester United", "portugese"],
            "Kobe": ["Kobe Briant", 37, "Lakers", "american"],
            "Sadio": ["Sadio Mané", 29, "Liverpool", "senegalese"],
            "Zlatan":["Zlatan Ibrahimovic", 41, "Milan AC", "sweeden"],
            "Messi": ["Leo Messi", 33, "PSG", "argentin"]}

db_columns=["name", "age", "club", "nationality"]

def build_df(dico_data=players):
    data=[line_ for line_ in players.values() ]
    return pd.DataFrame(data=data, columns=db_columns)



if __name__== "__main__":
    #db_connect()
    is_date()
    print("hello")
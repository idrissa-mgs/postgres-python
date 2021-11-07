import pandas as pd
import numpy as np

from db.db_function import load_data, db_connect



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
    db_connect()
import os
import pandas as pd
import numpy as np
from datetime import datetime
from dateutil.parser import parse
import click

from main import engine


from db.db_function import  db_connect, read_sql




def convert_date(ts):
    if not ts:
        return None
    else:
        try:
            dt = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            if dt < datetime.now():
                return dt
            else:
                return None
        except:
            return None


def read_and_process_data():
    tables = ["customers", "orders", "products", "items"]
    dict_df = {}
    for tab in tables:
        df = pd.read_csv(f"data/{tab}.csv")
        df = df.where(pd.notnull(df), None).replace({np.nan: None})
        if tab == "customers":
            df["customer_zip_code_prefix"] = df["customer_zip_code_prefix"].apply(lambda x : str(x).split(".")[0] if x else x)
            df.drop_duplicates(subset=["customer_id"], inplace=True)
            df.dropna(subset=["customer_id"], inplace=True)
        if tab == "orders":
            order_status = [
                "delivered",
                "invoiced",
                "shipped",
                "processing",
                "unavailable",
                "canceled",
                "created",
                "approved",
            ]
            date_cols = [
                "order_purchase_timestamp",
                "order_approved_at",
                "order_delivered_carrier_date",
                "order_delivered_customer_date",
                "order_estimated_delivery_date",
            ]
            df = df[df["order_status"].isin(order_status)]
            df.dropna(subset=["order_id", "customer_id"], inplace=True)
            for col in date_cols:
                df[col] = df[col].apply(convert_date)
        if tab == "items":
            df["shipping_limit_date"] = df["shipping_limit_date"].apply(convert_date)
        dict_df[tab] = df

    return dict_df


def create_tables():
    create_stat = read_sql("src/db/create_db.sql")
    conn = db_connect()
    cur = conn.cursor()
    cur.execute(create_stat)
    conn.close()

def load_tables():

    tables_df_dict = read_and_process_data()
    for table in ["customers","products", "orders","items"]:
        df = tables_df_dict[table]
        df.to_sql(
            name=table, con=engine, if_exists="append", index=False, schema="e_commerce"
        )

if __name__=="__main__":
    create_tables()
    load_tables()
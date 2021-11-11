import os
import click
from db.db_function import db_connect



@click.command()
@click.option("--schema-name", default="e_commerce", help="schema to drop")
def drop_schema(schema_name):
    conn = db_connect()
    query = f"DROP SCHEMA {schema_name} CASCADE;"
    cur = conn.cursor()
    cur.execute(query)
    conn.close()


if __name__== "__main__":
    drop_schema()
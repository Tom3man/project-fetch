import functools
import getpass
import os
from datetime import datetime
from typing import Union

import pandas as pd

from project_fetch import DATA_PATH
from project_fetch.tables import TaggingDatabase


def with_database_connection(func):
    """Decorator to handle the database connection lifecycle."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tag = TaggingDatabase(database_path=DATA_PATH)
        tag.create_table(overwrite=False)
        try:
            return func(tag, *args, **kwargs)
        finally:
            # Disconnect from database
            del tag
    return wrapper


@with_database_connection
def add_to_db(tag, url: str, question: int, response: Union[str, None]):
    """Add data to the database."""
    user = getpass.getuser()
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if response:
        response = str(response).lower()
    df = pd.DataFrame(columns=TaggingDatabase.DEFAULT_SCHEMA.keys())
    df.loc[len(df)] = [time_now, user, url, question, response]

    tag.ingest_dataframe(df=df)


def with_csv_connection(func):
    """Decorator to handle the database connection lifecycle."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        db_path = f"{DATA_PATH}/{TaggingDatabase.DEFAULT_PATH}.csv"
        if not os.path.exists(db_path):
            # Build csv
            df_csv = pd.DataFrame(
                columns=list(TaggingDatabase.DEFAULT_SCHEMA.keys()))
            df_csv.to_csv(db_path, index=False)

        else:
            df_csv = pd.read_csv(db_path)

        try:
            return func(df_csv, *args, **kwargs)
        finally:
            df_csv.to_csv(db_path, index=False)

    return wrapper


@with_csv_connection
def add_to_csv(df_csv, url: str, question: int, response: str):
    """Add data to the database."""
    user = getpass.getuser()
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if response:
        response = str(response).lower()

    df_csv.loc[len(df_csv)] = [time_now, user, url, question, response]

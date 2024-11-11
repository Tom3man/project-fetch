import functools
import getpass
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

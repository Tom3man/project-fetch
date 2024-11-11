from typing import Dict, List

from sqlite_forge.database import SqliteDatabase


class TaggingDatabase(SqliteDatabase):

    DEFAULT_PATH: str = "TAGGING"
    PRIMARY_KEY: List[str] = ["load_date"]
    DEFAULT_SCHEMA: Dict[str, str] = {
        "load_date": "datetime",
        "user": "varchar(50)",
        "image_url": "varchar(200)",
        "question": "integer",
        "response": "varchar(200)",
    }

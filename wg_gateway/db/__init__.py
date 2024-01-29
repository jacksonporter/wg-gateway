"""
Package init for the shared `db` lib
"""

from __future__ import annotations
from typing import Any
from wg_gateway.db.database import Database

from wg_gateway.db.dynamodb import DynamoDBDatabase


SUPPORTED_DATABASE_TYPES = {"dynamodb": DynamoDBDatabase}


def get_and_init_db(database_type: str, db_options: dict[str, Any]) -> Database:
    """
    Gets an appropriate DB object to work with based on passed on CLI args
    """
    if database_type not in SUPPORTED_DATABASE_TYPES:
        raise ValueError(
            f"database_type {database_type} is not a supported "
            f"database type. Options: {', '.join(SUPPORTED_DATABASE_TYPES.keys())}"
        )

    return SUPPORTED_DATABASE_TYPES[database_type](**db_options)

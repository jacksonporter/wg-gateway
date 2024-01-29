from __future__ import annotations
from typing import Any, Iterator

from wg_gateway.db.config import DBConfiguration


class Database:
    """
    Defines a database object (allows for interchanging databases)
    """

    database_config: DBConfiguration

    def __init__(self, database_config: DBConfiguration, *args, **kwargs) -> None:
        if not database_config or not isinstance(database_config, DBConfiguration):
            raise ValueError(
                "Database was not passed any configuration or was of the wrong type!"
            )
        self.database_config = database_config

    def get_config_keys(self) -> set[str]:
        """
        Returns the keys in this configuration
        """
        required_keys = self.database_config.required_attrs.get_keys()
        optional_keys = self.database_config.optional_attrs.get_keys()

        return set().union(required_keys).union(optional_keys)

    def get_config_value(self, key: str, default_value: Any = None) -> Any:
        """
        Returns a database configuration value
        """
        if key in self.database_config.required_attrs.get_keys():
            return self.database_config.required_attrs.get_value(key)

        val = self.database_config.optional_attrs.get_value(key)

        return val if val else default_value

    def get_config_values(self, keys_to_ignore: set[str] = None) -> Iterator:
        """
        Returns a database configuration value
        """
        keys_to_ignore = keys_to_ignore if keys_to_ignore else set()

        for key in self.get_config_keys():
            if key not in keys_to_ignore:
                yield key, self.get_config_value(key)

    def has_config_value(self, key: str, allow_none: bool = False) -> bool:
        """
        Determines if Database configuration has a specific key with value
        """
        return key in self.get_config_keys() and (
            allow_none or self.get_config_value(key)
        )

    def bootstrap(self, *args, **kwargs) -> Database:
        """
        Configures a database for initial use
        """
        raise NotImplementedError("This method must be overridden!")

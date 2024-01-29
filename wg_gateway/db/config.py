from __future__ import annotations
from typing import Any


class DBConfigurationAttributes:
    """
    Defines a set of Database Configuration Attributes and options for
    validating/getting such attributes.
    """

    attrs: dict[str, Any]

    def __init__(self, required_keys: bool, **kwargs) -> None:
        if kwargs:
            self.attrs = {str(k): v for k, v, in kwargs.items() if required_keys or v}  # type: ignore
        else:
            self.attrs = {}

    def validate_required(self) -> DBConfigurationAttributes:
        """
        Validates all attr keys have truthy values
        """
        keys_missing_values = set()

        for k, v in self.attrs.items():
            if not v:
                keys_missing_values.add(k)

        if keys_missing_values:
            raise ValueError(
                f"The following keys were missing values: {', '.join(keys_missing_values)}"
            )

        return self

    def validate_types(
        self, type_dict: dict[str, type], is_optional: bool = False
    ) -> DBConfigurationAttributes:
        """
        Checks the type of a value
        """
        keys_with_wrong_value_type = set()

        for k, v in self.attrs.items():
            if (not is_optional and v) and not isinstance(v, type_dict[k]):
                keys_with_wrong_value_type.add(k)

        if keys_with_wrong_value_type:
            raise ValueError(
                f"The following keys were had wrongly typed values! {', '.join(keys_with_wrong_value_type)}"
            )

        return self

    def get_keys(self) -> set[str]:
        """
        Returns the keys in this configuration
        """
        return set(self.attrs.keys())

    def get_value(self, key: str, default_value: Any = None) -> Any:
        """
        Returns a database configuration value
        """
        return self.attrs.get(key, default_value)

    def has_value(self, key: str, allow_none: bool = False) -> bool:
        """
        Determines if Database configuration has a specific key with value
        """
        return key in self.attrs and (allow_none or self.get_value(key))


class DBConfiguration:
    """
    Defines sets of Database Configuration Attributes (required and optional)
    with validating/getting such attributes.
    """

    required_attrs: DBConfigurationAttributes
    optional_attrs: DBConfigurationAttributes

    def __init__(
        self,
        required_attrs: DBConfigurationAttributes,
        required_attrs_types: dict[str, type],
        optional_attrs: DBConfigurationAttributes,
        optional_attrs_types: dict[str, type],
    ) -> None:
        self.required_attrs = required_attrs.validate_required().validate_types(
            required_attrs_types
        )
        self.optional_attrs = optional_attrs.validate_types(
            optional_attrs_types, is_optional=True
        )

    def validate(self, *args, **kwargs) -> DBConfiguration:
        """
        Method to validate that optional arguments are valid
        Override for more complex logic
        """
        return self  # defaults to passing validation (please override as needed)

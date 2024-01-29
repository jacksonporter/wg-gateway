"""
Package init for DynamoDB Configurations
"""
from logging import getLogger
from typing import TYPE_CHECKING, override

from boto3 import Session
import boto3

from wg_gateway import LOGGER_NAME
from wg_gateway.db.config import DBConfiguration, DBConfigurationAttributes
from wg_gateway.db.database import Database


if TYPE_CHECKING:
    from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource
else:
    DynamoDBServiceResource = object


LOGGER = getLogger(LOGGER_NAME)


class DynamoDBDatabaseConfiguration(DBConfiguration):
    """
    Defines a configuration object to work with DynamoDB
    """

    def __init__(
        self,
        endpoint_url: str | None = None,
        aws_access_key_id: str | None = None,
        aws_secret_access_key: str | None = None,
        region_name: str | None = None,
        profile_name: str | None = None,
        boto3_session: Session | None = None,
    ) -> None:
        super().__init__(
            required_attrs=DBConfigurationAttributes(
                required_keys=True,
                region_name=region_name,
            ),
            required_attrs_types={
                "region_name": str,
            },
            optional_attrs=DBConfigurationAttributes(
                required_keys=False,
                endpoint_url=endpoint_url,
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_secret_access_key,
                profile_name=profile_name,
                boto3_session=boto3_session,

            ),
            optional_attrs_types={
                "endpoint_url": str,
                "aws_access_key_id": str,
                "aws_secret_access_key": str,
                "profile_name": str,
                "boto3_session": Session,
            },
        )

    @override
    def validate(self, *args, **kwargs) -> DBConfiguration:
        if not self.optional_attrs.has_value("endpoint_url"):
            LOGGER.warning(
                "endpoint_url was not specified, going to assume DDB URL from AWS credentials"
            )

        if not self.optional_attrs.has_value("boto3_session"):
            if not self.optional_attrs.has_value("region_name"):
                LOGGER.warning(
                    "region_name was not specified, going to let boto3 (AWS SDK) handle it!"
                )

            if not (
                (
                    self.optional_attrs.has_value("aws_access_key_id"),
                    self.optional_attrs.has_value("aws_secret_access_key"),
                )
                or (self.optional_attrs.has_value("profile_name"),)
            ):
                LOGGER.warning(
                        "aws_access_key_id, aws_secret_access_key or profile_name were not"
                        " specified, going to let boto3 (AWS SDK) handle it!"
                )
        else:
            LOGGER.info(
                "boto3.Session was provided, going to use that object to work with DDB."
            )

        return super().validate(*args, **kwargs)


class DynamoDBDatabase(Database):
    """
    Defines interface for working with DynamoDB
    """

    database_config: DynamoDBDatabaseConfiguration
    ddb_resource: DynamoDBServiceResource

    def __init__(self, *args, **kwargs) -> None:
        ddb_config = DynamoDBDatabaseConfiguration(*args, **kwargs)

        super().__init__(ddb_config, *args, **kwargs)

        have_boto3_session = self.has_config_value("boto3_session", allow_none=True)

        if have_boto3_session:
            boto3_session = self.get_config_value("boto3_session")
            print("Found boto3 session")
            self.ddb_resource = boto3_session.resource("dynamodb")
        else:
            self.ddb_resource = boto3.resource(
                "dynamodb", **dict(self.get_config_values())
            )

    @override
    def bootstrap(self, *args, **kwargs) -> Database:
        """
        Configures a DDB database for initial use
        """
        wg_interfaces_table = self.ddb_resource.create_table(
            TableName="wiregaurd-gateway-interfaces",
            KeySchema=[{"AttributeName": "interfaceName", "KeyType": "HASH"}],
            AttributeDefinitions=[
                {"AttributeName": "interfaceName", "AttributeType": "S"}
                {"AttributeName": "address", "AttributeType": "S"}
                {"AttributeName": "privateKey", "AttributeType": "S"}
                {"AttributeName": "publicKey", "AttributeType": "S"}
                {"AttributeName": "postUp", "AttributeType": "S"}
                {"AttributeName": "postDown", "AttributeType": "S"}
            ],
            BillingMode="PAY_PER_REQUEST",
            TableClass="STANDARD",
        )
        print(wg_interfaces_table.table_status)

        wg_peers_table = self.ddb_resource.create_table(
            TableName="wiregaurd-gateway-interfaces",
            KeySchema=[{"AttributeName": "interfaceName", "KeyType": "HASH"}],
            AttributeDefinitions=[
                {"AttributeName": "interfaceName", "AttributeType": "S"}
            ],
            BillingMode="PAY_PER_REQUEST",
            TableClass="STANDARD",
        )
        print(wg_interfaces_table.table_status)

        return self

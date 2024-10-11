from abc import ABC, abstractmethod
from enum import Enum

class DataBaseType(Enum):
    POSTGRESQL = "pg"
    MSSQLSERVER = "sqlserver"
    MYSQL = "mysql"

class DatabaseConnector(ABC):
    @abstractmethod
    def connect(self):
        raise NotImplementedError
    
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

class PostgreSQLConnector(DatabaseConnector):
    def connect(self):
        print(f"> Connected to a PostgreSQL database via {self.connection_string}")


class MSSQLServerConnector(DatabaseConnector):
    def connect(self):
        print(f"> Connected to a MS SQL Server database via {self.connection_string}")


class MySQLConnector(DatabaseConnector):
    def connect(self):
        print(f"> Connected to a MySQL database via {self.connection_string}")

class DatabaseConnectorFactory:
    def create_database(self, connector_type: Enum):
        if connector_type == DataBaseType.POSTGRESQL:
            return PostgreSQLConnector(connection_string="postgresql://localhost:5432")
        elif connector_type == DataBaseType.MSSQLSERVER:
            return MSSQLServerConnector(connection_string="mssql://localhost:1433")
        elif connector_type == DataBaseType.MYSQL:
            return MySQLConnector(connection_string="mysql://localhost:3306")
        else:
            raise ValueError(f"Unknown database connector: {connector_type}")

if __name__ == '__main__':
    factory = DatabaseConnectorFactory()

    postgresql = factory.create_database(connector_type=DataBaseType.POSTGRESQL)
    sqlserver = factory.create_database(connector_type=DataBaseType.MSSQLSERVER)
    mysql = factory.create_database(connector_type=DataBaseType.MYSQL)

    postgresql.connect()
    sqlserver.connect()
    mysql.connect()

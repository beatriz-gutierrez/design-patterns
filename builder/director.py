from builders.sql_query_builder import SQLQueryBuilder
from builders.postgres_query_builder import PostgresSQLQueryBuilder
from typing import List, Optional
from enum import Enum

# The director controls the building process using a builder instance.
# We will have as many builders as SQL dialects (MySQL, PostgreSQL, BigQuery, etc.)


# Predefined methods for building specific types of queries
class QueryType(Enum):
    SQLQueryBuilder = "SQLQueryBuilder"
    PostgresSQLQueryBuilder = "PostgresSQLQueryBuilder"


class Director:

    def __init__(
        self, builder_type: Optional[QueryType] = None
    ) -> None:
        if builder_type == QueryType.SQLQueryBuilder:
            self.builder = SQLQueryBuilder()
        elif builder_type == QueryType.PostgresSQLQueryBuilder:
            self.builder = PostgresSQLQueryBuilder()
        else:
            raise ValueError("Invalid builder type")

    @property
    def get_builder(self):
        return self.builder

    def build_simple_select_query(self, table: str, columns: List[str]) -> str:
        return self.builder.reset().select(table, columns).get_query()

    def build_select_with_where(
        self, table: str, columns: List[str], condition: str
    ) -> str:
        return self.builder.reset().select(table, columns).where(condition).get_query()

    def build_select_with_order_by(
        self,
        table: str,
        columns: List[str],
        condition: str,
        order_column: str,
        order: str,
    ) -> str:
        return (
            self.builder.reset()
            .select(table, columns)
            .where(condition)
            .order_by(order_column, order)
            .get_query()
        )

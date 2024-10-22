from sql_query_builder import SQLQueryBuilder
from postgres_query_builder import PostgresSQLQueryBuilder
from typing import List, Optional
from enum import Enum

# The director controls the building process using a builder instance.
# We will have as many builders as SQL dialects (MySQL, PostgreSQL, BigQuery, etc.)
# TODO: check if this idea is correct


# Predefined methods for building specific types of queries
class QueryType(Enum):
    SQLQueryBuilder = "SQLQueryBuilder"
    PostgresSQLQueryBuilder = "PostgresSQLQueryBuilder"


class Director:

    # TODO: is it correct to pass the builder type as a parameter?
    def __init__(
        self, builder_type: Optional[QueryType] = QueryType.SQLQueryBuilder
    ) -> None:
        if builder_type == QueryType.SQLQueryBuilder:
            self.builder = SQLQueryBuilder()
        elif builder_type == QueryType.PostgresSQLQueryBuilder:
            self.builder = PostgresSQLQueryBuilder()
        else:
            raise ValueError("Invalid builder type")

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

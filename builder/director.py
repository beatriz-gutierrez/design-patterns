from sql_query_builder import SQLQueryBuilder
from typing import List

# The director controls the building process using a builder instance.
# We will have as many builders as SQL dialects (MySQL, PostgreSQL, BigQuery, etc.)


# Predefined methods for building specific types of queries


def build_simple_select_query(self, table: str, columns: List[str]) -> str:
    return self.reset().select(table, columns).get_query()


def build_select_with_where(
    self, table: str, columns: List[str], condition: str
) -> str:
    return self.reset().select(table, columns).where(condition).get_query()


def build_select_with_order_by(
    self, table: str, columns: List[str], condition: str, order_column: str, order: str
) -> str:
    return (
        self.reset()
        .select(table, columns)
        .where(condition)
        .order_by(order_column, order)
        .get_query()
    )

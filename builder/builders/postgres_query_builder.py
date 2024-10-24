from sql_query import SQLQuery
from typing import List, Optional
from builders.query_builder import QueryBuilder

# Most methods return self to allow method chaining
# (very typical in the Builder pattern)

# This updated class includes some PostgreSQL-specific features:
# - ilike method for case-insensitive pattern matching.
# - returning method to specify columns to return after an INSERT,
# UPDATE, or DELETE operation.


class PostgresSQLQueryBuilder(QueryBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> "PostgresSQLQueryBuilder":
        self._query = SQLQuery()
        self._base_query = ""
        return self

    def select(self, table: str, columns: List[str]) -> "PostgresSQLQueryBuilder":
        columns_part = ", ".join(columns)
        self._base_query = f"SELECT {columns_part} FROM {table}"
        return self

    def where(self, condition: str) -> "PostgresSQLQueryBuilder":
        self._base_query += f" WHERE {condition}"
        return self

    def where_and_clause(self, condition: str) -> "PostgresSQLQueryBuilder":
        self._base_query += f" AND {condition}"
        return self

    def order_by(
        self, column: str, order: Optional[str] = "ASC"
    ) -> "PostgresSQLQueryBuilder":
        self._base_query += f" ORDER BY {column} {order}"
        return self

    def limit(self, limit: int) -> "PostgresSQLQueryBuilder":
        self._base_query += f" LIMIT {limit}"
        return self

    def pattern_match(self, column: str, pattern: str) -> "PostgresSQLQueryBuilder":
        self._base_query += f" WHERE {column} ILIKE '{pattern}'"
        return self

    # "builder" method
    def get_query(self) -> str:
        self._query.set_query(self._base_query)
        return self._query.get_query()

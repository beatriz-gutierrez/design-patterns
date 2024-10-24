from sql_query import SQLQuery
from typing import List, Optional
from builders.query_builder import QueryBuilder

# Most methods return self to allow method chaining
# (very typical in the Builder pattern)

class SQLQueryBuilder(QueryBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> "SQLQueryBuilder":
        self._base_query = ""
        return self

    def select(self, table: str, columns: List[str]) -> "SQLQueryBuilder":
        columns_part = ", ".join(columns)
        self._base_query = f"SELECT {columns_part} FROM {table}"
        return self

    def where(self, condition: str) -> "SQLQueryBuilder":
        self._base_query += f" WHERE {condition}"
        return self

    def where_and_clause(self, condition: str) -> "SQLQueryBuilder":
        self._base_query += f" AND {condition}"
        return self

    def order_by(self, column: str, order: Optional[str] = "ASC") -> "SQLQueryBuilder":
        self._base_query += f" ORDER BY {column} {order}"
        return self

    def limit(self, limit: int) -> "SQLQueryBuilder":
        self._base_query += f" LIMIT {limit}"
        return self

    def pattern_match(self, column: str, pattern: str) -> "SQLQueryBuilder":
        self._base_query += f" WHERE {column} LIKE '{pattern}'"
        return self

    def get_query(self) -> str:
        # delegate the instantiation to the end
        query = SQLQuery()
        query.set_query(self._base_query)
        return query.get_query()

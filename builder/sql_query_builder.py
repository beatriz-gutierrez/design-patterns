from sql_query import SQLQuery
from typing import List, Optional

# Most methods return self to allow method chaining
# (very typical in the Builder pattern)


class SQLQueryBuilder:
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> "SQLQueryBuilder":
        self._query = SQLQuery()
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

    # "builder" method
    def get_query(self) -> str:
        self._query.set_query(self._base_query)
        return self._query.get_query()

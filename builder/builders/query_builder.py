from sql_query import SQLQuery
from typing import List, Optional
from abc import ABC, abstractmethod

# Most methods return self to allow method chaining
# (very typical in the Builder pattern)


class QueryBuilder(ABC):
    def reset(self) -> "QueryBuilder":
        raise NotImplementedError("This method is not implemented in an abstract class.")

    def select(self, table: str, columns: List[str]) -> "QueryBuilder":
        raise NotImplementedError("This method is not implemented in an abstract class.")

    def where(self, condition: str) -> "QueryBuilder":
        raise NotImplementedError("This method is not implemented in an abstract class.")

    def where_and_clause(self, condition: str) -> "QueryBuilder":
        raise NotImplementedError("This method is not implemented in an abstract class.")

    def order_by(self, column: str, order: Optional[str] = "ASC") -> "QueryBuilder":
        raise NotImplementedError("This method is not implemented in an abstract class.")

    def limit(self, limit: int) -> "QueryBuilder":
        raise NotImplementedError("This method is not implemented in an abstract class.")

    def pattern_match(self, column: str, pattern: str) -> "QueryBuilder":
        raise NotImplementedError(
            "This method is not implemented in an abstract class."
        )
    
    def get_query(self) -> str:
        raise NotImplementedError(
            "This method is not implemented in an abstract class."
        )

from sql_query import SQLQuery
from typing import List, Optional
from abc import ABC, abstractmethod

# Most methods return self to allow method chaining
# (very typical in the Builder pattern)


class QueryBuilder(ABC):
    @abstractmethod
    def reset(self) -> "QueryBuilder":
        raise NotImplementedError("This method is not implemented in an abstract class.")

    @abstractmethod
    def select(self, table: str, columns: List[str]) -> "QueryBuilder":
        raise NotImplementedError("This method is not implemented in an abstract class.")

    @abstractmethod
    def where(self, condition: str) -> "QueryBuilder":
        raise NotImplementedError("This method is not implemented in an abstract class.")

    @abstractmethod
    def where_and_clause(self, condition: str) -> "QueryBuilder":
        raise NotImplementedError("This method is not implemented in an abstract class.")

    @abstractmethod
    def order_by(self, column: str, order: Optional[str] = "ASC") -> "QueryBuilder":
        raise NotImplementedError("This method is not implemented in an abstract class.")

    @abstractmethod
    def limit(self, limit: int) -> "QueryBuilder":
        raise NotImplementedError("This method is not implemented in an abstract class.")

    @abstractmethod
    def pattern_match(self, column: str, pattern: str) -> "QueryBuilder":
        raise NotImplementedError(
            "This method is not implemented in an abstract class."
        )

    @abstractmethod
    def get_query(self) -> str:
        raise NotImplementedError(
            "This method is not implemented in an abstract class."
        )

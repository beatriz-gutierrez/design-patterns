from dataclasses import dataclass

@dataclass
class SQLQuery:

    query: str = ""

    def set_query(self, query: str) -> None:
        self.query = query

    def get_query(self) -> str:
        return self.query

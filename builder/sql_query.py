class SQLQuery:
    def __init__(self) -> None:
        self.query = ""

    def set_query(self, query: str) -> None:
        self.query = query

    def get_query(self) -> str:
        return self.query

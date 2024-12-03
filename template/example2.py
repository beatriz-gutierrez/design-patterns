import sqlite3
import datetime
import os

"""
Template steps:
1.- connect to the database
2.- construct the query (for new vehicles or gross sales)
3.- run the query
4.- format the results in a comma-delimited string
5.- output the data to a file or email (for new vehicles or gross sales)
"""
class QueryTemplate:

    def __init__(self):
        self.db_path = os.path.join("template", "sales.db")
        
        if not os.path.exists(self.db_path):
            self.create_bbdd()

    def create_bbdd(self):
        conn = sqlite3.connect(self.db_path)

        conn.execute(
            "CREATE TABLE Sales (salesperson text, "
            "amt currency, year integer, model text, new boolean)"
        )
        conn.execute("INSERT INTO Sales values" " ('Tim', 16000, 2010, 'Honda Fit', 'true')")
        conn.execute("INSERT INTO Sales values" " ('Tim', 9000, 2006, 'Ford Focus', 'false')")
        conn.execute("INSERT INTO Sales values" " ('Gayle', 8000, 2004, 'Dodge Neon', 'false')")
        conn.execute(
            "INSERT INTO Sales values" " ('Gayle', 28000, 2009, 'Ford Mustang', 'true')"
        )
        conn.execute(
            "INSERT INTO Sales values" " ('Gayle', 50000, 2010, 'Lincoln Navigator', 'true')"
        )
        conn.execute(
            "INSERT INTO Sales values" " ('Don', 20000, 2008, 'Toyota Prius', 'false')"
        )
        conn.commit()
        conn.close()

    def connect(self):
        self.conn = sqlite3.connect(self.db_path)

    def construct_query(self):
        raise NotImplementedError()

    def do_query(self):
        results = self.conn.execute(self.query)
        self.results = results.fetchall()

    def format_results(self):
        output = []
        for row in self.results:
            row = [str(i) for i in row]
            output.append(", ".join(row))
        self.formatted_results = "\n".join(output)

    def output_results(self):
        raise NotImplementedError()

    def process_format(self):
        self.connect()
        self.construct_query()
        self.do_query()
        self.format_results()
        self.output_results()


class NewVehiclesQuery(QueryTemplate):
    def construct_query(self):
        self.query = "select * from Sales where new='true'"

    def output_results(self):
        print(self.formatted_results)


class UserGrossQuery(QueryTemplate):
    def construct_query(self):
        self.query = (
            "select salesperson, sum(amt) " + " from Sales group by salesperson"
        )

    def output_results(self):
        filename = f"gross_sales_{datetime.date.today().strftime('%Y%m%d')}"
        with open(os.path.join("template", filename), "w") as outfile:
            outfile.write(self.formatted_results)


if __name__ == "__main__":

    new_vehicles = NewVehiclesQuery()
    new_vehicles.process_format()

    users_gross = UserGrossQuery()
    users_gross.process_format()

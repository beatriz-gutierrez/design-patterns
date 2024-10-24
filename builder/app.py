from director import Director, QueryType

if __name__ == "__main__":
    director = Director(builder_type=QueryType.SQLQueryBuilder)

    print("SQL queries")

    print(director.build_simple_select_query("table", ["column1", "column2"]))
    print(
        director.build_select_with_where(
            "table", ["column1", "column2"], "column1 = 'value'"
        )
    )
    print(
        director.build_select_with_order_by(
            "users",
            ["id", "name", "email"],
            "id < 100",
            "id",
            "ASC",
        )
    )

    # non-prefined queries
    print(
        director.get_builder.reset()
        .select("users", ["id", "name", "email"])
        .where("id < 100")
        .pattern_match("email", "%@gmail.com")
        .where_and_clause("email IS NULL")
        .limit(10)
        .get_query()
    )

    print("PostgresSQL queries")
    director2 = Director(builder_type=QueryType.PostgresSQLQueryBuilder)

    print(
        director2.build_select_with_order_by(
            "users",
            ["id", "name", "email"],
            "id < 100",
            "id",
            "ASC",
        )
    )

    # non-prefined queries
    print(
        director2.get_builder.reset()
        .select("users", ["id", "name", "email"])
        .where("id < 100")
        .pattern_match("email", "%@gmail.com")
        .where_and_clause("email IS NULL")
        .limit(10)
        .get_query()
    )

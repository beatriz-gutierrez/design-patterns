from director import Director, QueryType

if __name__ == "__main__":
    director = Director()

    print("SQL queries")
    # queries
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

    # TODO: this way to call the builder is correct?
    # non-prefined queries
    print(
        director.builder.reset()
        .select("users", ["id", "name", "email"])
        .where("id < 100")
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

    # TODO: this way to call the builder is correct?
    # non-prefined queries
    print(
        director2.builder.reset()
        .select("users", ["id", "name", "email"])
        .where("id < 100")
        .ilike("email", "%@gmail.com")
        .where_and_clause("email IS NULL")
        .limit(10)
        .get_query()
    )

import strawberry

from sbplay.resolvers import Query

schema = strawberry.Schema(query=Query)


def test_query():
    query = """
        query TestQuery($title: String!) {
            books(title: $title) {
                title
                author
            }
        }
    """

    result = schema.execute_sync(
        query,
        variable_values={"title": "The Great Gatsby"},
    )

    assert result.errors is None
    assert result.data["books"] == [
        {
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
        }
    ]

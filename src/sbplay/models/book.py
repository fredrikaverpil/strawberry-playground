import strawberry


@strawberry.type
class BookType:
    title: str
    author: str

import typing

import strawberry

from sbplay.models.book import Book
from sbplay.models.user import UserType
from sbplay.services.books import get_books
from sbplay.services.users import get_users


@strawberry.type
class Query:
    books: typing.List[Book] = strawberry.field(resolver=get_books)
    users: typing.List[UserType] = strawberry.field(resolver=get_users)

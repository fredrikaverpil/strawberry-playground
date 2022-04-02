from typing import List, Optional

import strawberry

from sbplay.models.book import Book
from sbplay.models.user import UserType
from sbplay.services.books import get_books
from sbplay.services.users import get_users


@strawberry.type
class Query:
    @strawberry.field
    def books(self, title: Optional[str] = None) -> List[Book]:
        return get_books(title)

    users: List[UserType] = strawberry.field(resolver=get_users)

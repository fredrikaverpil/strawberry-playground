from typing import List, Optional

from sbplay.models.book import BookType

BOOKS = [
    BookType(
        title="The Great Gatsby",
        author="F. Scott Fitzgerald",
    ),
    BookType(
        title="The Lord Of The Rings",
        author="J.R.R. Tolkien",
    ),
]


def get_books(title: Optional[str]) -> List[BookType]:
    if not title:
        return BOOKS

    return [book for book in BOOKS if book.title.lower() == title.lower()]

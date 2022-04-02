from typing import List, Optional

from sbplay.models.book import Book

BOOKS = [
    Book(
        title="The Great Gatsby",
        author="F. Scott Fitzgerald",
    ),
    Book(
        title="The Lord Of The Rings",
        author="J.R.R. Tolkien",
    ),
]


def get_books(title: Optional[str]) -> List[Book]:
    if not title:
        return BOOKS

    return [book for book in BOOKS if book.title == title]

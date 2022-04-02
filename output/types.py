from typing import List, Optional

class MyQueryResultBooks:
    title: str
    author: str

class MyQueryResultUsers:
    id: int
    name: str
    friends: Optional[List[int]]

class MyQueryResult:
    books: List[MyQueryResultBooks]
    users: List[MyQueryResultUsers]
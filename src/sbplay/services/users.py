from collections import namedtuple
from datetime import datetime, timezone

from sbplay.models.user import User, UserType


def get_users_from_db():
    """This simulates fetching from db."""
    user = namedtuple("User", ["id", "name", "signup_ts", "friends"])
    return [
        user(
            id=1,
            name="John",
            signup_ts=datetime.now(timezone.utc),
            friends=[2, 3],
        ),
        user(
            id=2,
            name="Maria",
            signup_ts=datetime.now(timezone.utc),
            friends=[1],
        ),
        user(
            id=3,
            name="Bo",
            signup_ts=datetime.now(timezone.utc),
            friends=[1],
        ),
    ]


def validate_users(users):
    """Validate db data with pydantic."""
    return [
        User(
            id=user.id,
            name=user.name,
            signup_ts=user.signup_ts,
            friends=user.friends,
        )
        for user in users
    ]


def get_users():
    return [
        UserType(
            id=user.id,
            name=user.name,
            friends=user.friends,
        )
        for user in validate_users(get_users_from_db())
    ]

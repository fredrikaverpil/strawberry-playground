from datetime import datetime
from typing import List, Optional

import strawberry
from pydantic import BaseModel, validator


class User(BaseModel):
    id: int
    name: str
    signup_ts: Optional[datetime] = None
    friends: List[int] = []

    @validator("name")
    def name_cannot_contain_space(cls, v):
        if " " in v:
            raise ValueError("must not contain a space")
        return v


@strawberry.experimental.pydantic.type(model=User)
class UserType:
    """Strawberry User model.

    Notes:
        Provide `all_fields=True` in the decorator signature to inherit
        all fields but this might not be desireable, as too much could
        be exposed in the API.
    """

    id: strawberry.auto
    name: strawberry.auto
    friends: strawberry.auto

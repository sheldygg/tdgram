from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class Users(BaseType):
    """
    Represents a list of users
    """

    __type__: Literal["users"] = "users"

    total_count: int
    """Approximate total number of users found"""
    user_ids: list[int]
    """A list of user identifiers"""

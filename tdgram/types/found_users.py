from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class FoundUsers(BaseType):
    """
    Represents a list of found users
    """

    __type__: Literal["foundUsers"] = "foundUsers"

    user_ids: list[int]
    """Identifiers of the found users"""
    next_offset: str
    """The offset for the next request. If empty, then there are no more results"""

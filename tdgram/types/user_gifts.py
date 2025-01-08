from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import UserGift


@dataclass(kw_only=True)
class UserGifts(BaseType):
    """
    Represents a list of gifts received by a user
    """

    __type__: Literal["userGifts"] = "userGifts"

    total_count: int
    """The total number of received gifts"""
    gifts: list[UserGift]
    """The list of gifts"""
    next_offset: str
    """The offset for the next request. If empty, then there are no more results"""

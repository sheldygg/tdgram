from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import AddedReaction


@dataclass(kw_only=True)
class AddedReactions(BaseType):
    """
    Represents a list of reactions added to a message
    """

    __type__: Literal["addedReactions"] = "addedReactions"

    total_count: int
    """The total number of found reactions"""
    reactions: list[AddedReaction]
    """The list of added reactions"""
    next_offset: str
    """The offset for the next request. If empty, then there are no more results"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Story


@dataclass(kw_only=True)
class FoundStories(BaseType):
    """
    Contains a list of stories found by a search
    """

    __type__: Literal["foundStories"] = "foundStories"

    total_count: int
    """Approximate total number of stories found"""
    stories: list[Story]
    """List of stories"""
    next_offset: str
    """The offset for the next request. If empty, then there are no more results"""

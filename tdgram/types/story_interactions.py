from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import StoryInteraction


@dataclass(kw_only=True)
class StoryInteractions(BaseType):
    """
    Represents a list of interactions with a story
    """

    __type__: Literal["storyInteractions"] = "storyInteractions"

    total_count: int
    """Approximate total number of interactions found"""
    total_forward_count: int
    """Approximate total number of found forwards and reposts; always 0 for chat stories"""
    total_reaction_count: int
    """Approximate total number of found reactions; always 0 for chat stories"""
    interactions: list[StoryInteraction]
    """List of story interactions"""
    next_offset: str
    """The offset for the next request. If empty, then there are no more results"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Story


@dataclass(kw_only=True)
class Stories(BaseType):
    """
    Represents a list of stories
    """

    __type__: Literal["stories"] = "stories"

    total_count: int
    """Approximate total number of stories found"""
    stories: list[Story]
    """The list of stories"""
    pinned_story_ids: list[int]
    """Identifiers of the pinned stories; returned only in getChatPostedToChatPageStories with from_story_id == 0"""

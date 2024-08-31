from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StoryInfo(BaseType):
    """
    Contains basic information about a story
    """

    __type__: Literal["storyInfo"] = "storyInfo"

    story_id: int
    """Unique story identifier among stories of the given sender"""
    date: int
    """Point in time (Unix timestamp) when the story was published"""
    is_for_close_friends: bool
    """True, if the story is available only to close friends"""

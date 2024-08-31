from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StoryInteractionInfo(BaseType):
    """
    Contains information about interactions with a story
    """

    __type__: Literal["storyInteractionInfo"] = "storyInteractionInfo"

    view_count: int
    """Number of times the story was viewed"""
    forward_count: int
    """Number of times the story was forwarded; 0 if none or unknown"""
    reaction_count: int
    """Number of reactions added to the story; 0 if none or unknown"""
    recent_viewer_user_ids: list[int]
    """Identifiers of at most 3 recent viewers of the story"""

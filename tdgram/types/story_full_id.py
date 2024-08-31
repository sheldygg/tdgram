from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StoryFullId(BaseType):
    """
    Contains identifier of a story along with identifier of its sender
    """

    __type__: Literal["storyFullId"] = "storyFullId"

    sender_chat_id: int
    """Identifier of the chat that posted the story"""
    story_id: int
    """Unique story identifier among stories of the given sender"""

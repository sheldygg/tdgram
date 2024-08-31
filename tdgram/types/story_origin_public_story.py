from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StoryOriginPublicStory(BaseType):
    """
    The original story was a public story with known sender
    """

    __type__: Literal["storyOriginPublicStory"] = "storyOriginPublicStory"

    chat_id: int
    """Identifier of the chat that posted original story"""
    story_id: int
    """Story identifier of the original story"""

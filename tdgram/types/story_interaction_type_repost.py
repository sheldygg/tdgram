from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Story


@dataclass(kw_only=True)
class StoryInteractionTypeRepost(BaseType):
    """
    A repost of the story as a story
    """

    __type__: Literal["storyInteractionTypeRepost"] = "storyInteractionTypeRepost"

    story: Story
    """The reposted story"""

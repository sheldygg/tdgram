from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Story


@dataclass(kw_only=True)
class PublicForwardStory(BaseType):
    """
    Contains a public repost to a story
    """

    __type__: Literal["publicForwardStory"] = "publicForwardStory"

    story: Story
    """Information about the story"""

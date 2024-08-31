from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import StoryAreaPosition, StoryAreaType


@dataclass(kw_only=True)
class StoryArea(BaseType):
    """
    Describes a clickable rectangle area on a story media
    """

    __type__: Literal["storyArea"] = "storyArea"

    position: StoryAreaPosition
    """Position of the area"""
    type: StoryAreaType
    """Type of the area"""

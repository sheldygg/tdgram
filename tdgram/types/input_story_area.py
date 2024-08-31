from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputStoryAreaType, StoryAreaPosition


@dataclass(kw_only=True)
class InputStoryArea(BaseType):
    """
    Describes a clickable rectangle area on a story media to be added
    """

    __type__: Literal["inputStoryArea"] = "inputStoryArea"

    position: StoryAreaPosition
    """Position of the area"""
    type: InputStoryAreaType
    """Type of the area"""

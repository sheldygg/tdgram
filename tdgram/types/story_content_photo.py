from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Photo


@dataclass(kw_only=True)
class StoryContentPhoto(BaseType):
    """
    A photo story
    """

    __type__: Literal["storyContentPhoto"] = "storyContentPhoto"

    photo: Photo
    """The photo"""

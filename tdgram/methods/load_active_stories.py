from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, StoryList
from .base import BaseMethod


@dataclass(kw_only=True)
class LoadActiveStories(BaseMethod):
    """
    Loads more active stories from a story list. The loaded stories will be sent through updates. Active stories are sorted by
    """

    __type__: Literal["loadActiveStories"] = "loadActiveStories"
    __returning_type__ = Ok

    story_list: StoryList
    """The story list in which to load active stories"""

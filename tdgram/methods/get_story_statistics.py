from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import StoryStatistics
from .base import BaseMethod


@dataclass(kw_only=True)
class GetStoryStatistics(BaseMethod):
    """
    Returns detailed statistics about a story. Can be used only if story.can_get_statistics == true
    """

    __type__: Literal["getStoryStatistics"] = "getStoryStatistics"
    __returning_type__ = StoryStatistics

    chat_id: int
    """Chat identifier"""
    story_id: int
    """Story identifier"""
    is_dark: bool
    """Pass true if a dark theme is used by the application"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ReactionType


@dataclass(kw_only=True)
class StoryAreaTypeSuggestedReaction(BaseType):
    """
    An area pointing to a suggested reaction. App needs to show a clickable reaction on the area and call setStoryReaction when the are is clicked
    """

    __type__: Literal["storyAreaTypeSuggestedReaction"] = "storyAreaTypeSuggestedReaction"

    reaction_type: ReactionType
    """Type of the reaction"""
    total_count: int
    """Number of times the reaction was added"""
    is_dark: bool
    """True, if reaction has a dark background"""
    is_flipped: bool
    """True, if reaction corner is flipped"""

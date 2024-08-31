from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ReactionType


@dataclass(kw_only=True)
class InputStoryAreaTypeSuggestedReaction(BaseType):
    """
    An area pointing to a suggested reaction
    """

    __type__: Literal["inputStoryAreaTypeSuggestedReaction"] = (
        "inputStoryAreaTypeSuggestedReaction"
    )

    reaction_type: ReactionType
    """Type of the reaction"""
    is_dark: bool
    """True, if reaction has a dark background"""
    is_flipped: bool
    """True, if reaction corner is flipped"""

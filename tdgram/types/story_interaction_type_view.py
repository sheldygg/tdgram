from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ReactionType


@dataclass(kw_only=True)
class StoryInteractionTypeView(BaseType):
    """
    A view of the story
    """

    __type__: Literal["storyInteractionTypeView"] = "storyInteractionTypeView"

    chosen_reaction_type: ReactionType | None = None
    """Type of the reaction that was chosen by the viewer; may be null if none"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import BlockList, MessageSender, StoryInteractionType


@dataclass(kw_only=True)
class StoryInteraction(BaseType):
    """
    Represents interaction with a story
    """

    __type__: Literal["storyInteraction"] = "storyInteraction"

    actor_id: MessageSender
    """Identifier of the user or chat that made the interaction"""
    interaction_date: int
    """Approximate point in time (Unix timestamp) when the interaction happened"""
    block_list: BlockList | None = None
    """Block list to which the actor is added; may be null if none or for chat stories"""
    type: StoryInteractionType
    """Type of the interaction"""

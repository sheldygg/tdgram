from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import AvailableReaction, ReactionUnavailabilityReason


@dataclass(kw_only=True)
class AvailableReactions(BaseType):
    """
    Represents a list of reactions that can be added to a message
    """

    __type__: Literal["availableReactions"] = "availableReactions"

    top_reactions: list[AvailableReaction]
    """List of reactions to be shown at the top"""
    recent_reactions: list[AvailableReaction]
    """List of recently used reactions"""
    popular_reactions: list[AvailableReaction]
    """List of popular reactions"""
    allow_custom_emoji: bool
    """True, if any custom emoji reaction can be added by Telegram Premium subscribers"""
    are_tags: bool
    """True, if the reactions will be tags and the message can be found by them"""
    unavailability_reason: ReactionUnavailabilityReason | None = None
    """The reason why the current user can't add reactions to the message, despite some other users can; may be null if none"""

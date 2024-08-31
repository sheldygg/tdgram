from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageSender, ReactionType


@dataclass(kw_only=True)
class AddedReaction(BaseType):
    """
    Represents a reaction applied to a message
    """

    __type__: Literal["addedReaction"] = "addedReaction"

    type: ReactionType
    """Type of the reaction"""
    sender_id: MessageSender
    """Identifier of the chat member, applied the reaction"""
    is_outgoing: bool
    """True, if the reaction was added by the current user"""
    date: int
    """Point in time (Unix timestamp) when the reaction was added"""

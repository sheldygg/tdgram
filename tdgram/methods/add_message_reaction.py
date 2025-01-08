from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, ReactionType
from .base import BaseMethod


@dataclass(kw_only=True)
class AddMessageReaction(BaseMethod):
    """
    Adds a reaction or a tag to a message. Use getMessageAvailableReactions to receive the list of available reactions for the message
    """

    __type__: Literal["addMessageReaction"] = "addMessageReaction"
    __returning_type__ = Ok

    chat_id: int
    """Identifier of the chat to which the message belongs"""
    message_id: int
    """Identifier of the message"""
    reaction_type: ReactionType
    """Type of the reaction to add. Use addPendingPaidMessageReaction instead to add the paid reaction"""
    is_big: bool
    """Pass true if the reaction is added with a big animation"""
    update_recent_reactions: bool
    """Pass true if the reaction needs to be added to recent reactions; tags are never added to the list of recent reactions"""

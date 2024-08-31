from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageSender, ReactionType


@dataclass(kw_only=True)
class UpdateMessageReaction(BaseType):
    """
    User changed its reactions on a message with public reactions; for bots only
    """

    __type__: Literal["updateMessageReaction"] = "updateMessageReaction"

    chat_id: int
    """Chat identifier"""
    message_id: int
    """Message identifier"""
    actor_id: MessageSender
    """Identifier of the user or chat that changed reactions"""
    date: int
    """Point in time (Unix timestamp) when the reactions were changed"""
    old_reaction_types: list[ReactionType]
    """Old list of chosen reactions"""
    new_reaction_types: list[ReactionType]
    """New list of chosen reactions"""

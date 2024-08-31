from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, ReactionType
from .base import BaseMethod


@dataclass(kw_only=True)
class RemoveMessageReaction(BaseMethod):
    """
    Removes a reaction from a message. A chosen reaction can always be removed
    """

    __type__: Literal["removeMessageReaction"] = "removeMessageReaction"
    __returning_type__ = Ok

    chat_id: int
    """Identifier of the chat to which the message belongs"""
    message_id: int
    """Identifier of the message"""
    reaction_type: ReactionType
    """Type of the reaction to remove. The paid reaction can't be removed"""

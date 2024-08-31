from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, ReactionType
from .base import BaseMethod


@dataclass(kw_only=True)
class SetMessageReactions(BaseMethod):
    """
    Sets reactions on a message; for bots only
    """

    __type__: Literal["setMessageReactions"] = "setMessageReactions"
    __returning_type__ = Ok

    chat_id: int
    """Identifier of the chat to which the message belongs"""
    message_id: int
    """Identifier of the message"""
    reaction_types: list[ReactionType]
    """Types of the reaction to set"""
    is_big: bool
    """Pass true if the reactions are added with a big animation"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageReaction


@dataclass(kw_only=True)
class UpdateMessageReactions(BaseType):
    """
    Reactions added to a message with anonymous reactions have changed; for bots only
    """

    __type__: Literal["updateMessageReactions"] = "updateMessageReactions"

    chat_id: int
    """Chat identifier"""
    message_id: int
    """Message identifier"""
    date: int
    """Point in time (Unix timestamp) when the reactions were changed"""
    reactions: list[MessageReaction]
    """The list of reactions added to the message"""

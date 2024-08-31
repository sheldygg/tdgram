from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import UnreadReaction


@dataclass(kw_only=True)
class UpdateMessageUnreadReactions(BaseType):
    """
    The list of unread reactions added to a message was changed
    """

    __type__: Literal["updateMessageUnreadReactions"] = "updateMessageUnreadReactions"

    chat_id: int
    """Chat identifier"""
    message_id: int
    """Message identifier"""
    unread_reactions: list[UnreadReaction]
    """The new list of unread reactions"""
    unread_reaction_count: int
    """The new number of messages with unread reactions left in the chat"""

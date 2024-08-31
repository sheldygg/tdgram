from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageSender, ReactionType


@dataclass(kw_only=True)
class UnreadReaction(BaseType):
    """
    Contains information about an unread reaction to a message
    """

    __type__: Literal["unreadReaction"] = "unreadReaction"

    type: ReactionType
    """Type of the reaction"""
    sender_id: MessageSender
    """Identifier of the sender, added the reaction"""
    is_big: bool
    """True, if the reaction was added with a big animation"""

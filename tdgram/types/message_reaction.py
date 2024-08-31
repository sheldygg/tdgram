from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageSender, ReactionType


@dataclass(kw_only=True)
class MessageReaction(BaseType):
    """
    Contains information about a reaction to a message
    """

    __type__: Literal["messageReaction"] = "messageReaction"

    type: ReactionType
    """Type of the reaction"""
    total_count: int
    """Number of times the reaction was added"""
    is_chosen: bool
    """True, if the reaction is chosen by the current user"""
    used_sender_id: MessageSender | None = None
    """Identifier of the message sender used by the current user to add the reaction; may be null if unknown or the reaction isn't chosen"""
    recent_sender_ids: list[MessageSender]
    """Identifiers of at most 3 recent message senders, added the reaction; available in private, basic group and supergroup chats"""

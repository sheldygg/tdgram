from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageSender


@dataclass(kw_only=True)
class ForwardSource(BaseType):
    """
    Contains information about the last message from which a new message was forwarded last time
    """

    __type__: Literal["forwardSource"] = "forwardSource"

    chat_id: int
    """Identifier of the chat to which the message that was forwarded belonged; may be 0 if unknown"""
    message_id: int
    """Identifier of the message; may be 0 if unknown"""
    sender_id: MessageSender | None = None
    """Identifier of the sender of the message; may be null if unknown or the new message was forwarded not to Saved Messages"""
    sender_name: str
    """Name of the sender of the message if the sender is hidden by their privacy settings"""
    date: int
    """Point in time (Unix timestamp) when the message is sent; 0 if unknown"""
    is_outgoing: bool
    """True, if the message that was forwarded is outgoing; always false if sender is unknown"""

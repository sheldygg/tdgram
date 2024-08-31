from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageContent, MessageOrigin, TextQuote


@dataclass(kw_only=True)
class MessageReplyToMessage(BaseType):
    """
    Describes a message replied by a given message
    """

    __type__: Literal["messageReplyToMessage"] = "messageReplyToMessage"

    chat_id: int
    """The identifier of the chat to which the message belongs; may be 0 if the replied message is in unknown chat"""
    message_id: int
    """The identifier of the message; may be 0 if the replied message is in unknown chat"""
    quote: TextQuote | None = None
    """Chosen quote from the replied message; may be null if none"""
    origin: MessageOrigin | None = None
    """Information about origin of the message if the message was from another chat or topic; may be null for messages from the same chat"""
    origin_send_date: int
    """Point in time (Unix timestamp) when the message was sent if the message was from another chat or topic; 0 for messages from the same chat"""
    content: MessageContent | None = None
    """Media content of the message if the message was from another chat or topic; may be null for messages from the same chat and messages without media."""

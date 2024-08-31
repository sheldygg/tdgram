from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageSender


@dataclass(kw_only=True)
class MessageReplyInfo(BaseType):
    """
    Contains information about replies to a message
    """

    __type__: Literal["messageReplyInfo"] = "messageReplyInfo"

    reply_count: int
    """Number of times the message was directly or indirectly replied"""
    recent_replier_ids: list[MessageSender]
    """Identifiers of at most 3 recent repliers to the message; available in channels with a discussion supergroup. The users and chats are expected to be inaccessible: only their photo and name will be available"""
    last_read_inbox_message_id: int
    """Identifier of the last read incoming reply to the message"""
    last_read_outbox_message_id: int
    """Identifier of the last read outgoing reply to the message"""
    last_message_id: int
    """Identifier of the last reply to the message"""

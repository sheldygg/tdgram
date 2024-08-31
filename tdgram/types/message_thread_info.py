from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import DraftMessage, Message, MessageReplyInfo


@dataclass(kw_only=True)
class MessageThreadInfo(BaseType):
    """
    Contains information about a message thread
    """

    __type__: Literal["messageThreadInfo"] = "messageThreadInfo"

    chat_id: int
    """Identifier of the chat to which the message thread belongs"""
    message_thread_id: int
    """Message thread identifier, unique within the chat"""
    reply_info: MessageReplyInfo | None = None
    """Information about the message thread; may be null for forum topic threads"""
    unread_message_count: int
    """Approximate number of unread messages in the message thread"""
    messages: list[Message]
    """The messages from which the thread starts. The messages are returned in reverse chronological order (i.e., in order of decreasing message_id)"""
    draft_message: DraftMessage | None = None
    """A draft of a message in the message thread; may be null if none"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Count, SearchMessagesFilter
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatMessageCount(BaseMethod):
    """
    Returns approximate number of messages of the specified type in the chat
    """

    __type__: Literal["getChatMessageCount"] = "getChatMessageCount"
    __returning_type__ = Count

    chat_id: int
    """Identifier of the chat in which to count messages"""
    filter: SearchMessagesFilter
    """Filter for message content; searchMessagesFilterEmpty is unsupported in this function"""
    saved_messages_topic_id: int
    """If not 0, only messages in the specified Saved Messages topic will be counted; pass 0 to count all messages, or for chats other than Saved Messages"""
    return_local: bool
    """Pass true to get the number of messages without sending network requests, or -1 if the number of messages is unknown locally"""

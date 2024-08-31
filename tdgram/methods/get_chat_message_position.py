from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Count, SearchMessagesFilter
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatMessagePosition(BaseMethod):
    """
    Returns approximate 1-based position of a message among messages, which can be found by the specified filter in the chat. Cannot be used in secret chats
    """

    __type__: Literal["getChatMessagePosition"] = "getChatMessagePosition"
    __returning_type__ = Count

    chat_id: int
    """Identifier of the chat in which to find message position"""
    message_id: int
    """Message identifier"""
    filter: SearchMessagesFilter
    """Filter for message content; searchMessagesFilterEmpty, searchMessagesFilterUnreadMention, searchMessagesFilterUnreadReaction, and searchMessagesFilterFailedToSend are unsupported in this function"""
    message_thread_id: int
    """If not 0, only messages in the specified thread will be considered; supergroups only"""
    saved_messages_topic_id: int
    """If not 0, only messages in the specified Saved Messages topic will be considered; pass 0 to consider all relevant messages, or for chats other than Saved Messages"""

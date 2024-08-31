from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MessageCalendar, SearchMessagesFilter
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatMessageCalendar(BaseMethod):
    """
    Returns information about the next messages of the specified type in the chat split by days. Returns the results in reverse chronological order. Can return partial result for the last returned day. Behavior of this method depends on the value of the option 'utc_time_offset'
    """

    __type__: Literal["getChatMessageCalendar"] = "getChatMessageCalendar"
    __returning_type__ = MessageCalendar

    chat_id: int
    """Identifier of the chat in which to return information about messages"""
    filter: SearchMessagesFilter
    """Filter for message content. Filters searchMessagesFilterEmpty, searchMessagesFilterMention, searchMessagesFilterUnreadMention, and searchMessagesFilterUnreadReaction are unsupported in this function"""
    from_message_id: int
    """The message identifier from which to return information about messages; use 0 to get results from the last message"""
    saved_messages_topic_id: int
    """If not0, only messages in the specified Saved Messages topic will be considered; pass 0 to consider all messages, or for chats other than Saved Messages"""

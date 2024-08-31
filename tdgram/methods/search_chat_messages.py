from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FoundChatMessages, MessageSender, SearchMessagesFilter
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchChatMessages(BaseMethod):
    """
    Searches for messages with given words in the chat. Returns the results in reverse chronological order, i.e. in order of decreasing message_id. Cannot be used in secret chats with a non-empty query
    """

    __type__: Literal["searchChatMessages"] = "searchChatMessages"
    __returning_type__ = FoundChatMessages

    chat_id: int
    """Identifier of the chat in which to search messages"""
    query: str
    """Query to search for"""
    sender_id: MessageSender | None = None
    """Identifier of the sender of messages to search for; pass null to search for messages from any sender. Not supported in secret chats"""
    from_message_id: int
    """Identifier of the message starting from which history must be fetched; use 0 to get results from the last message"""
    offset: int
    """Specify 0 to get results from exactly the message from_message_id or a negative offset to get the specified message and some newer messages"""
    limit: int
    """The maximum number of messages to be returned; must be positive and can't be greater than 100. If the offset is negative, the limit must be greater than -offset."""
    filter: SearchMessagesFilter | None = None
    """Additional filter for messages to search; pass null to search for all messages"""
    message_thread_id: int
    """If not 0, only messages in the specified thread will be returned; supergroups only"""
    saved_messages_topic_id: int
    """If not 0, only messages in the specified Saved Messages topic will be returned; pass 0 to return all messages, or for chats other than Saved Messages"""

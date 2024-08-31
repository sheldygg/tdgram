from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatList, FoundMessages, SearchMessagesFilter
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchMessages(BaseMethod):
    """
    Searches for messages in all chats except secret chats. Returns the results in reverse chronological order (i.e., in order of decreasing (date, chat_id, message_id)).
    """

    __type__: Literal["searchMessages"] = "searchMessages"
    __returning_type__ = FoundMessages

    chat_list: ChatList | None = None
    """Chat list in which to search messages; pass null to search in all chats regardless of their chat list. Only Main and Archive chat lists are supported"""
    only_in_channels: bool
    """Pass true to search only for messages in channels"""
    query: str
    """Query to search for"""
    offset: str
    """Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results"""
    limit: int
    """The maximum number of messages to be returned; up to 100. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit"""
    filter: SearchMessagesFilter | None = None
    """Additional filter for messages to search; pass null to search for all messages. Filters searchMessagesFilterMention, searchMessagesFilterUnreadMention, searchMessagesFilterUnreadReaction, searchMessagesFilterFailedToSend, and searchMessagesFilterPinned are unsupported in this function"""
    min_date: int
    """If not 0, the minimum date of the messages to return"""
    max_date: int
    """If not 0, the maximum date of the messages to return"""

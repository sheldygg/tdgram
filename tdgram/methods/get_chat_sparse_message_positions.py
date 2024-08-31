from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MessagePositions, SearchMessagesFilter
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatSparseMessagePositions(BaseMethod):
    """
    Returns sparse positions of messages of the specified type in the chat to be used for shared media scroll implementation. Returns the results in reverse chronological order (i.e., in order of decreasing message_id).
    """

    __type__: Literal["getChatSparseMessagePositions"] = "getChatSparseMessagePositions"
    __returning_type__ = MessagePositions

    chat_id: int
    """Identifier of the chat in which to return information about message positions"""
    filter: SearchMessagesFilter
    """Filter for message content. Filters searchMessagesFilterEmpty, searchMessagesFilterMention, searchMessagesFilterUnreadMention, and searchMessagesFilterUnreadReaction are unsupported in this function"""
    from_message_id: int
    """The message identifier from which to return information about message positions"""
    limit: int
    """The expected number of message positions to be returned; 50-2000. A smaller number of positions can be returned, if there are not enough appropriate messages"""
    saved_messages_topic_id: int
    """If not 0, only messages in the specified Saved Messages topic will be considered; pass 0 to consider all messages, or for chats other than Saved Messages"""

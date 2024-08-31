from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FoundChatMessages, ReactionType
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchSavedMessages(BaseMethod):
    """
    Searches for messages tagged by the given reaction and with the given words in the Saved Messages chat; for Telegram Premium users only.
    """

    __type__: Literal["searchSavedMessages"] = "searchSavedMessages"
    __returning_type__ = FoundChatMessages

    saved_messages_topic_id: int
    """If not 0, only messages in the specified Saved Messages topic will be considered; pass 0 to consider all messages"""
    tag: ReactionType | None = None
    """Tag to search for; pass null to return all suitable messages"""
    query: str
    """Query to search for"""
    from_message_id: int
    """Identifier of the message starting from which messages must be fetched; use 0 to get results from the last message"""
    offset: int
    """Specify 0 to get results from exactly the message from_message_id or a negative offset to get the specified message and some newer messages"""
    limit: int
    """The maximum number of messages to be returned; must be positive and can't be greater than 100. If the offset is negative, the limit must be greater than -offset."""

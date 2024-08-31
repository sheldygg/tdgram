from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ForumTopics
from .base import BaseMethod


@dataclass(kw_only=True)
class GetForumTopics(BaseMethod):
    """
    Returns found forum topics in a forum chat. This is a temporary method for getting information about topic list from the server
    """

    __type__: Literal["getForumTopics"] = "getForumTopics"
    __returning_type__ = ForumTopics

    chat_id: int
    """Identifier of the forum chat"""
    query: str
    """Query to search for in the forum topic's name"""
    offset_date: int
    """The date starting from which the results need to be fetched. Use 0 or any date in the future to get results from the last topic"""
    offset_message_id: int
    """The message identifier of the last message in the last found topic, or 0 for the first request"""
    offset_message_thread_id: int
    """The message thread identifier of the last found topic, or 0 for the first request"""
    limit: int
    """The maximum number of forum topics to be returned; up to 100. For optimal performance, the number of returned forum topics is chosen by TDLib and can be smaller than the specified limit"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatEventLogFilters, ChatEvents
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatEventLog(BaseMethod):
    """
    Returns a list of service actions taken by chat members and administrators in the last 48 hours. Available only for supergroups and channels. Requires administrator rights. Returns results in reverse chronological order (i.e., in order of decreasing event_id)
    """

    __type__: Literal["getChatEventLog"] = "getChatEventLog"
    __returning_type__ = ChatEvents

    chat_id: int
    """Chat identifier"""
    query: str
    """Search query by which to filter events"""
    from_event_id: int
    """Identifier of an event from which to return results. Use 0 to get results from the latest events"""
    limit: int
    """The maximum number of events to return; up to 100"""
    filters: ChatEventLogFilters | None = None
    """The types of events to return; pass null to get chat events of all types"""
    user_ids: list[int]
    """User identifiers by which to filter events. By default, events relating to all users will be returned"""

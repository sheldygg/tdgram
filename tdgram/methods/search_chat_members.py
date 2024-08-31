from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatMembers, ChatMembersFilter
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchChatMembers(BaseMethod):
    """
    Searches for a specified query in the first name, last name and usernames of the members of a specified chat. Requires administrator rights if the chat is a channel
    """

    __type__: Literal["searchChatMembers"] = "searchChatMembers"
    __returning_type__ = ChatMembers

    chat_id: int
    """Chat identifier"""
    query: str
    """Query to search for"""
    limit: int
    """The maximum number of users to be returned; up to 200"""
    filter: ChatMembersFilter | None = None
    """The type of users to search for; pass null to search among all chat members"""

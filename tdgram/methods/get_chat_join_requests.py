from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatJoinRequest, ChatJoinRequests
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatJoinRequests(BaseMethod):
    """
    Returns pending join requests in a chat
    """

    __type__: Literal["getChatJoinRequests"] = "getChatJoinRequests"
    __returning_type__ = ChatJoinRequests

    chat_id: int
    """Chat identifier"""
    invite_link: str
    """Invite link for which to return join requests. If empty, all join requests will be returned. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links"""
    query: str
    """A query to search for in the first names, last names and usernames of the users to return"""
    offset_request: ChatJoinRequest | None = None
    """A chat join request from which to return next requests; pass null to get results from the beginning"""
    limit: int
    """The maximum number of requests to join the chat to return"""

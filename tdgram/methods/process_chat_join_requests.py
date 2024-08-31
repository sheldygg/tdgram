from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ProcessChatJoinRequests(BaseMethod):
    """
    Handles all pending join requests for a given link in a chat
    """

    __type__: Literal["processChatJoinRequests"] = "processChatJoinRequests"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    invite_link: str
    """Invite link for which to process join requests. If empty, all join requests will be processed. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links"""
    approve: bool
    """Pass true to approve all requests; pass false to decline them"""

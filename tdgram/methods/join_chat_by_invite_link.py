from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Chat
from .base import BaseMethod


@dataclass(kw_only=True)
class JoinChatByInviteLink(BaseMethod):
    """
    Uses an invite link to add the current user to the chat if possible. May return an error with a message 'INVITE_REQUEST_SENT' if only a join request was created
    """

    __type__: Literal["joinChatByInviteLink"] = "joinChatByInviteLink"
    __returning_type__ = Chat

    invite_link: str
    """Invite link to use"""

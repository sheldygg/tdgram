from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FailedToAddMembers
from .base import BaseMethod


@dataclass(kw_only=True)
class AddChatMember(BaseMethod):
    """
    Adds a new member to a chat; requires can_invite_users member right. Members can't be added to private or secret chats. Returns information about members that weren't added
    """

    __type__: Literal["addChatMember"] = "addChatMember"
    __returning_type__ = FailedToAddMembers

    chat_id: int
    """Chat identifier"""
    user_id: int
    """Identifier of the user"""
    forward_limit: int
    """The number of earlier messages from the chat to be forwarded to the new member; up to 100. Ignored for supergroups and channels, or if the added user is a bot"""

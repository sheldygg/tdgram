from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatMemberStatus, MessageSender, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetChatMemberStatus(BaseMethod):
    """
    Changes the status of a chat member; requires can_invite_users member right to add a chat member, can_promote_members administrator right to change administrator rights of the member,
    """

    __type__: Literal["setChatMemberStatus"] = "setChatMemberStatus"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    member_id: MessageSender
    """Member identifier. Chats can be only banned and unbanned in supergroups and channels"""
    status: ChatMemberStatus
    """The new status of the member in the chat"""

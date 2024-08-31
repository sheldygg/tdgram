from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MessageSender, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class BanChatMember(BaseMethod):
    """
    Bans a member in a chat; requires can_restrict_members administrator right. Members can't be banned in private or secret chats. In supergroups and channels, the user will not be able to return to the group on their own using invite links, etc., unless unbanned first
    """

    __type__: Literal["banChatMember"] = "banChatMember"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    member_id: MessageSender
    """Member identifier"""
    banned_until_date: int
    """Point in time (Unix timestamp) when the user will be unbanned; 0 if never. If the user is banned for more than 366 days or for less than 30 seconds from the current time, the user is considered to be banned forever. Ignored in basic groups and if a chat is banned"""
    revoke_messages: bool
    """Pass true to delete all messages in the chat for the user that is being removed. Always true for supergroups and channels"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatMemberStatus, MessageSender


@dataclass(kw_only=True)
class ChatMember(BaseType):
    """
    Describes a user or a chat as a member of another chat
    """

    __type__: Literal["chatMember"] = "chatMember"

    member_id: MessageSender
    """Identifier of the chat member. Currently, other chats can be only Left or Banned. Only supergroups and channels can have other chats as Left or Banned members and these chats must be supergroups or channels"""
    inviter_user_id: int
    """Identifier of a user that invited/promoted/banned this member in the chat; 0 if unknown"""
    joined_chat_date: int
    """Point in time (Unix timestamp) when the user joined/was promoted/was banned in the chat"""
    status: ChatMemberStatus
    """Status of the member in the chat"""

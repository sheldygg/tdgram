from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import BotCommands, ChatInviteLink, ChatMember, ChatPhoto


@dataclass(kw_only=True)
class BasicGroupFullInfo(BaseType):
    """
    Contains full information about a basic group
    """

    __type__: Literal["basicGroupFullInfo"] = "basicGroupFullInfo"

    photo: ChatPhoto | None = None
    """Chat photo; may be null if empty or unknown. If non-null, then it is the same photo as in chat.photo"""
    description: str
    """Group description. Updated only after the basic group is opened"""
    creator_user_id: int
    """User identifier of the creator of the group; 0 if unknown"""
    members: list[ChatMember]
    """Group members"""
    can_hide_members: bool
    """True, if non-administrators and non-bots can be hidden in responses to getSupergroupMembers and searchChatMembers for non-administrators after upgrading the basic group to a supergroup"""
    can_toggle_aggressive_anti_spam: bool
    """True, if aggressive anti-spam checks can be enabled or disabled in the supergroup after upgrading the basic group to a supergroup"""
    invite_link: ChatInviteLink | None = None
    """Primary invite link for this group; may be null. For chat administrators with can_invite_users right only. Updated only after the basic group is opened"""
    bot_commands: list[BotCommands]
    """List of commands of bots in the group"""

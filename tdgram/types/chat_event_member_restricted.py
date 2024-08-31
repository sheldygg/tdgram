from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatMemberStatus, MessageSender


@dataclass(kw_only=True)
class ChatEventMemberRestricted(BaseType):
    """
    A chat member was restricted/unrestricted or banned/unbanned, or the list of their restrictions has changed
    """

    __type__: Literal["chatEventMemberRestricted"] = "chatEventMemberRestricted"

    member_id: MessageSender
    """Affected chat member identifier"""
    old_status: ChatMemberStatus
    """Previous status of the chat member"""
    new_status: ChatMemberStatus
    """New status of the chat member"""

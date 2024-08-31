from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatInviteLink


@dataclass(kw_only=True)
class ChatEventMemberJoinedByRequest(BaseType):
    """
    A new member was accepted to the chat by an administrator
    """

    __type__: Literal["chatEventMemberJoinedByRequest"] = "chatEventMemberJoinedByRequest"

    approver_user_id: int
    """User identifier of the chat administrator, approved user join request"""
    invite_link: ChatInviteLink | None = None
    """Invite link used to join the chat; may be null"""

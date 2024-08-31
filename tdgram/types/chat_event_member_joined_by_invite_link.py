from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatInviteLink


@dataclass(kw_only=True)
class ChatEventMemberJoinedByInviteLink(BaseType):
    """
    A new member joined the chat via an invite link
    """

    __type__: Literal["chatEventMemberJoinedByInviteLink"] = "chatEventMemberJoinedByInviteLink"

    invite_link: ChatInviteLink
    """Invite link used to join the chat"""
    via_chat_folder_invite_link: bool
    """True, if the user has joined the chat using an invite link for a chat folder"""

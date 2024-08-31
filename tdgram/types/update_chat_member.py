from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatInviteLink, ChatMember


@dataclass(kw_only=True)
class UpdateChatMember(BaseType):
    """
    User rights changed in a chat; for bots only
    """

    __type__: Literal["updateChatMember"] = "updateChatMember"

    chat_id: int
    """Chat identifier"""
    actor_user_id: int
    """Identifier of the user, changing the rights"""
    date: int
    """Point in time (Unix timestamp) when the user rights were changed"""
    invite_link: ChatInviteLink | None = None
    """If user has joined the chat using an invite link, the invite link; may be null"""
    via_join_request: bool
    """True, if the user has joined the chat after sending a join request and being approved by an administrator"""
    via_chat_folder_invite_link: bool
    """True, if the user has joined the chat using an invite link for a chat folder"""
    old_chat_member: ChatMember
    """Previous chat member"""
    new_chat_member: ChatMember
    """New chat member"""

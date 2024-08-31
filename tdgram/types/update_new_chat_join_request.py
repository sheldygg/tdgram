from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatInviteLink, ChatJoinRequest


@dataclass(kw_only=True)
class UpdateNewChatJoinRequest(BaseType):
    """
    A user sent a join request to a chat; for bots only
    """

    __type__: Literal["updateNewChatJoinRequest"] = "updateNewChatJoinRequest"

    chat_id: int
    """Chat identifier"""
    request: ChatJoinRequest
    """Join request"""
    user_chat_id: int
    """Chat identifier of the private chat with the user"""
    invite_link: ChatInviteLink | None = None
    """The invite link, which was used to send join request; may be null"""

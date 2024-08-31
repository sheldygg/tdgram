from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DeleteRevokedChatInviteLink(BaseMethod):
    """
    Deletes revoked chat invite links. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
    """

    __type__: Literal["deleteRevokedChatInviteLink"] = "deleteRevokedChatInviteLink"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    invite_link: str
    """Invite link to revoke"""

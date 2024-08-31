from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DeleteAllRevokedChatInviteLinks(BaseMethod):
    """
    Deletes all revoked chat invite links created by a given chat administrator. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
    """

    __type__: Literal["deleteAllRevokedChatInviteLinks"] = "deleteAllRevokedChatInviteLinks"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    creator_user_id: int
    """User identifier of a chat administrator, which links will be deleted. Must be an identifier of the current user for non-owner"""

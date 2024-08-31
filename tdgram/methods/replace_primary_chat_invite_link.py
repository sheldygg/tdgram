from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatInviteLink
from .base import BaseMethod


@dataclass(kw_only=True)
class ReplacePrimaryChatInviteLink(BaseMethod):
    """
    Replaces current primary invite link for a chat with a new primary invite link. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right
    """

    __type__: Literal["replacePrimaryChatInviteLink"] = "replacePrimaryChatInviteLink"
    __returning_type__ = ChatInviteLink

    chat_id: int
    """Chat identifier"""

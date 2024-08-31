from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatPermissions, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetChatPermissions(BaseMethod):
    """
    Changes the chat members permissions. Supported only for basic groups and supergroups. Requires can_restrict_members administrator right
    """

    __type__: Literal["setChatPermissions"] = "setChatPermissions"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    permissions: ChatPermissions
    """New non-administrator members permissions in the chat"""

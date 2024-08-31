from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleChatHasProtectedContent(BaseMethod):
    """
    Changes the ability of users to save, forward, or copy chat content. Supported only for basic groups, supergroups and channels. Requires owner privileges
    """

    __type__: Literal["toggleChatHasProtectedContent"] = "toggleChatHasProtectedContent"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    has_protected_content: bool
    """New value of has_protected_content"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateChatHasProtectedContent(BaseType):
    """
    A chat content was allowed or restricted for saving
    """

    __type__: Literal["updateChatHasProtectedContent"] = "updateChatHasProtectedContent"

    chat_id: int
    """Chat identifier"""
    has_protected_content: bool
    """New value of has_protected_content"""

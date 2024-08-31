from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetChatDescription(BaseMethod):
    """
    Changes information about a chat. Available for basic groups, supergroups, and channels. Requires can_change_info member right
    """

    __type__: Literal["setChatDescription"] = "setChatDescription"
    __returning_type__ = Ok

    chat_id: int
    """Identifier of the chat"""
    description: str
    """New chat description; 0-255 characters"""

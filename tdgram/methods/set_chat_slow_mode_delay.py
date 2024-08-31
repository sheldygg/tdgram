from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetChatSlowModeDelay(BaseMethod):
    """
    Changes the slow mode delay of a chat. Available only for supergroups; requires can_restrict_members right
    """

    __type__: Literal["setChatSlowModeDelay"] = "setChatSlowModeDelay"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    slow_mode_delay: int
    """New slow mode delay for the chat, in seconds; must be one of 0, 10, 30, 60, 300, 900, 3600"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BusinessBotManageBar(BaseType):
    """
    Contains information about a business bot that manages the chat
    """

    __type__: Literal["businessBotManageBar"] = "businessBotManageBar"

    bot_user_id: int
    """User identifier of the bot"""
    manage_url: str
    """URL to be opened to manage the bot"""
    is_bot_paused: bool
    """True, if the bot is paused. Use toggleBusinessConnectedBotChatIsPaused to change the value of the field"""
    can_bot_reply: bool
    """True, if the bot can reply"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleBotCanManageEmojiStatus(BaseMethod):
    """
    Toggles whether the bot can manage emoji status of the current user
    """

    __type__: Literal["toggleBotCanManageEmojiStatus"] = "toggleBotCanManageEmojiStatus"
    __returning_type__ = Ok

    bot_user_id: int
    """User identifier of the bot"""
    can_manage_emoji_status: bool
    """Pass true if the bot is allowed to change emoji status of the user; pass false otherwise"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleBotUsernameIsActive(BaseMethod):
    """
    Changes active state for a username of a bot. The editable username can't be disabled. May return an error with a message 'USERNAMES_ACTIVE_TOO_MUCH' if the maximum number of active usernames has been reached. Can be called only if userTypeBot.can_be_edited == true
    """

    __type__: Literal["toggleBotUsernameIsActive"] = "toggleBotUsernameIsActive"
    __returning_type__ = Ok

    bot_user_id: int
    """Identifier of the target bot"""
    username: str
    """The username to change"""
    is_active: bool
    """Pass true to activate the username; pass false to disable it"""

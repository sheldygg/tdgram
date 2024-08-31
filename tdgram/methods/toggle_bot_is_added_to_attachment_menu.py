from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleBotIsAddedToAttachmentMenu(BaseMethod):
    """
    Adds or removes a bot to attachment and side menu. Bot can be added to the menu, only if userTypeBot.can_be_added_to_attachment_menu == true
    """

    __type__: Literal["toggleBotIsAddedToAttachmentMenu"] = "toggleBotIsAddedToAttachmentMenu"
    __returning_type__ = Ok

    bot_user_id: int
    """Bot's user identifier"""
    is_added: bool
    """Pass true to add the bot to attachment menu; pass false to remove the bot from attachment menu"""
    allow_write_access: bool
    """Pass true if the current user allowed the bot to send them messages. Ignored if is_added is false"""

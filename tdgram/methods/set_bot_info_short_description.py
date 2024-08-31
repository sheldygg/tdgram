from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetBotInfoShortDescription(BaseMethod):
    """
    Sets the text shown on a bot's profile page and sent together with the link when users share the bot. Can be called only if userTypeBot.can_be_edited == true
    """

    __type__: Literal["setBotInfoShortDescription"] = "setBotInfoShortDescription"
    __returning_type__ = Ok

    bot_user_id: int
    """Identifier of the target bot"""
    language_code: str
    """A two-letter ISO 639-1 language code. If empty, the short description will be shown to all users for whose languages there is no dedicated description"""
    short_description: str
    """New bot's short description on the specified language"""

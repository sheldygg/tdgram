from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetBotInfoDescription(BaseMethod):
    """
    Sets the text shown in the chat with a bot if the chat is empty. Can be called only if userTypeBot.can_be_edited == true
    """

    __type__: Literal["setBotInfoDescription"] = "setBotInfoDescription"
    __returning_type__ = Ok

    bot_user_id: int
    """Identifier of the target bot"""
    language_code: str
    """A two-letter ISO 639-1 language code. If empty, the description will be shown to all users for whose languages there is no dedicated description"""
    description: str
    """New bot's description on the specified language"""

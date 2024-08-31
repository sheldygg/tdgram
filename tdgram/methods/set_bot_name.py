from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetBotName(BaseMethod):
    """
    Sets the name of a bot. Can be called only if userTypeBot.can_be_edited == true
    """

    __type__: Literal["setBotName"] = "setBotName"
    __returning_type__ = Ok

    bot_user_id: int
    """Identifier of the target bot"""
    language_code: str
    """A two-letter ISO 639-1 language code. If empty, the name will be shown to all users for whose languages there is no dedicated name"""
    name: str
    """New bot's name on the specified language; 0-64 characters; must be non-empty if language code is empty"""

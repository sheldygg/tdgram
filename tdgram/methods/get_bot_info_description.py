from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Text
from .base import BaseMethod


@dataclass(kw_only=True)
class GetBotInfoDescription(BaseMethod):
    """
    Returns the text shown in the chat with a bot if the chat is empty in the given language. Can be called only if userTypeBot.can_be_edited == true
    """

    __type__: Literal["getBotInfoDescription"] = "getBotInfoDescription"
    __returning_type__ = Text

    bot_user_id: int
    """Identifier of the target bot"""
    language_code: str
    """A two-letter ISO 639-1 language code or an empty string"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FormattedText
from .base import BaseMethod


@dataclass(kw_only=True)
class TranslateMessageText(BaseMethod):
    """
    Extracts text or caption of the given message and translates it to the given language. If the current user is a Telegram Premium user, then text formatting is preserved
    """

    __type__: Literal["translateMessageText"] = "translateMessageText"
    __returning_type__ = FormattedText

    chat_id: int
    """Identifier of the chat to which the message belongs"""
    message_id: int
    """Identifier of the message"""
    to_language_code: str
    """Language code of the language to which the message is translated. Must be one of"""

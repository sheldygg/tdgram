from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FormattedText
from .base import BaseMethod


@dataclass(kw_only=True)
class TranslateText(BaseMethod):
    """
    Translates a text to the given language. If the current user is a Telegram Premium user, then text formatting is preserved
    """

    __type__: Literal["translateText"] = "translateText"
    __returning_type__ = FormattedText

    text: FormattedText
    """Text to translate"""
    to_language_code: str
    """Language code of the language to which the message is translated. Must be one of"""

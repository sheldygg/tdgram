from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import EmojiKeywords
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchEmojis(BaseMethod):
    """
    Searches for emojis by keywords. Supported only if the file database is enabled. Order of results is unspecified
    """

    __type__: Literal["searchEmojis"] = "searchEmojis"
    __returning_type__ = EmojiKeywords

    text: str
    """Text to search for"""
    input_language_codes: list[str] | None = None
    """List of possible IETF language tags of the user's input language; may be empty if unknown"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FormattedText, TextParseMode
from .base import BaseMethod


@dataclass(kw_only=True)
class ParseTextEntities(BaseMethod):
    """
    Parses Bold, Italic, Underline, Strikethrough, Spoiler, CustomEmoji, BlockQuote, ExpandableBlockQuote, Code, Pre, PreCode, TextUrl
    """

    __type__: Literal["parseTextEntities"] = "parseTextEntities"
    __returning_type__ = FormattedText

    text: str
    """The text to parse"""
    parse_mode: TextParseMode
    """Text parse mode"""

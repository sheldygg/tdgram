from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText


@dataclass(kw_only=True)
class InputTextQuote(BaseType):
    """
    Describes manually chosen quote from another message
    """

    __type__: Literal["inputTextQuote"] = "inputTextQuote"

    text: FormattedText
    """Text of the quote; 0-getOption('message_reply_quote_length_max') characters. Only Bold, Italic, Underline, Strikethrough, Spoiler, and CustomEmoji entities are allowed to be kept and must be kept in the quote"""
    position: int
    """Quote position in the original message in UTF-16 code units"""

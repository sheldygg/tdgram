from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText


@dataclass(kw_only=True)
class TextQuote(BaseType):
    """
    Describes manually or automatically chosen quote from another message
    """

    __type__: Literal["textQuote"] = "textQuote"

    text: FormattedText
    """Text of the quote. Only Bold, Italic, Underline, Strikethrough, Spoiler, and CustomEmoji entities can be present in the text"""
    position: int
    """Approximate quote position in the original message in UTF-16 code units as specified by the message sender"""
    is_manual: bool
    """True, if the quote was manually chosen by the message sender"""

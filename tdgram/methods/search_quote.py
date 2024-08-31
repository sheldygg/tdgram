from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FormattedText, FoundPosition
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchQuote(BaseMethod):
    """
    Searches for a given quote in a text. Returns found quote start position in UTF-16 code units. Returns a 404 error if the quote is not found. Can be called synchronously
    """

    __type__: Literal["searchQuote"] = "searchQuote"
    __returning_type__ = FoundPosition

    text: FormattedText
    """Text in which to search for the quote"""
    quote: FormattedText
    """Quote to search for"""
    quote_position: int
    """Approximate quote position in UTF-16 code units"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FormattedText
from .base import BaseMethod


@dataclass(kw_only=True)
class ParseMarkdown(BaseMethod):
    """
    Parses Markdown entities in a human-friendly format, ignoring markup errors. Can be called synchronously
    """

    __type__: Literal["parseMarkdown"] = "parseMarkdown"
    __returning_type__ = FormattedText

    text: FormattedText
    """The text to parse. For example, '__italic__ ~~strikethrough~~ ||spoiler|| **bold** `code` ```pre``` __[italic__ text_url](telegram.org) __italic**bold italic__bold**'"""

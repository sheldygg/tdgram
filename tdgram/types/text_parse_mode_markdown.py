from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TextParseModeMarkdown(BaseType):
    """
    The text uses Markdown-style formatting
    """

    __type__: Literal["textParseModeMarkdown"] = "textParseModeMarkdown"

    version: int
    """Version of the parser: 0 or 1 - Telegram Bot API 'Markdown' parse mode, 2 - Telegram Bot API 'MarkdownV2' parse mode"""

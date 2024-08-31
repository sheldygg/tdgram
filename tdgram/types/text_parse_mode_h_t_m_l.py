from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TextParseModeHTML(BaseType):
    """
    The text uses HTML-style formatting. The same as Telegram Bot API 'HTML' parse mode
    """

    __type__: Literal["textParseModeHTML"] = "textParseModeHTML"

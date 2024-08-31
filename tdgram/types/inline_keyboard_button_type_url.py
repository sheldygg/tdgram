from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InlineKeyboardButtonTypeUrl(BaseType):
    """
    A button that opens a specified URL
    """

    __type__: Literal["inlineKeyboardButtonTypeUrl"] = "inlineKeyboardButtonTypeUrl"

    url: str
    """HTTP or tg:// URL to open. If the link is of the type internalLinkTypeWebApp, then the button must be marked as a Web App button"""

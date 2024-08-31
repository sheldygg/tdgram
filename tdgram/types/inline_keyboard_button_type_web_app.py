from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InlineKeyboardButtonTypeWebApp(BaseType):
    """
    A button that opens a Web App by calling openWebApp
    """

    __type__: Literal["inlineKeyboardButtonTypeWebApp"] = "inlineKeyboardButtonTypeWebApp"

    url: str
    """An HTTP URL to pass to openWebApp"""

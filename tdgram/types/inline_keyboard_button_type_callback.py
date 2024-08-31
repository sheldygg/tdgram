from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InlineKeyboardButtonTypeCallback(BaseType):
    """
    A button that sends a callback query to a bot
    """

    __type__: Literal["inlineKeyboardButtonTypeCallback"] = "inlineKeyboardButtonTypeCallback"

    data: bytes
    """Data to be sent to the bot via a callback query"""

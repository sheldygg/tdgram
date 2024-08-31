from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InlineKeyboardButtonTypeCallbackWithPassword(BaseType):
    """
    A button that asks for the 2-step verification password of the current user and then sends a callback query to a bot
    """

    __type__: Literal["inlineKeyboardButtonTypeCallbackWithPassword"] = (
        "inlineKeyboardButtonTypeCallbackWithPassword"
    )

    data: bytes
    """Data to be sent to the bot via a callback query"""

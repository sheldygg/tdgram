from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InlineKeyboardButtonTypeCallbackGame(BaseType):
    """
    A button with a game that sends a callback query to a bot. This button must be in the first column and row of the keyboard and can be attached only to a message with content of the type messageGame
    """

    __type__: Literal["inlineKeyboardButtonTypeCallbackGame"] = (
        "inlineKeyboardButtonTypeCallbackGame"
    )

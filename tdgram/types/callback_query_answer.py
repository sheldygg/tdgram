from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CallbackQueryAnswer(BaseType):
    """
    Contains a bot's answer to a callback query
    """

    __type__: Literal["callbackQueryAnswer"] = "callbackQueryAnswer"

    text: str
    """Text of the answer"""
    show_alert: bool
    """True, if an alert must be shown to the user instead of a toast notification"""
    url: str
    """URL to be opened"""

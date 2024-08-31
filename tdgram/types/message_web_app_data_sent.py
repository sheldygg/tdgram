from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageWebAppDataSent(BaseType):
    """
    Data from a Web App has been sent to a bot
    """

    __type__: Literal["messageWebAppDataSent"] = "messageWebAppDataSent"

    button_text: str
    """Text of the keyboardButtonTypeWebApp button, which opened the Web App"""

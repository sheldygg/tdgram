from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageWebAppDataReceived(BaseType):
    """
    Data from a Web App has been received; for bots only
    """

    __type__: Literal["messageWebAppDataReceived"] = "messageWebAppDataReceived"

    button_text: str
    """Text of the keyboardButtonTypeWebApp button, which opened the Web App"""
    data: str
    """The data"""

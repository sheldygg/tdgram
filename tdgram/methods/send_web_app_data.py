from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SendWebAppData(BaseMethod):
    """
    Sends data received from a keyboardButtonTypeWebApp Web App to a bot
    """

    __type__: Literal["sendWebAppData"] = "sendWebAppData"
    __returning_type__ = Ok

    bot_user_id: int
    """Identifier of the target bot"""
    button_text: str
    """Text of the keyboardButtonTypeWebApp button, which opened the Web App"""
    data: str
    """The data"""

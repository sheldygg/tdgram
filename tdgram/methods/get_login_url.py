from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import HttpUrl
from .base import BaseMethod


@dataclass(kw_only=True)
class GetLoginUrl(BaseMethod):
    """
    Returns an HTTP URL which can be used to automatically authorize the user on a website after clicking an inline button of type inlineKeyboardButtonTypeLoginUrl.
    """

    __type__: Literal["getLoginUrl"] = "getLoginUrl"
    __returning_type__ = HttpUrl

    chat_id: int
    """Chat identifier of the message with the button"""
    message_id: int
    """Message identifier of the message with the button"""
    button_id: int
    """Button identifier"""
    allow_write_access: bool
    """Pass true to allow the bot to send messages to the current user"""

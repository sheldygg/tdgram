from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import LoginUrlInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class GetLoginUrlInfo(BaseMethod):
    """
    Returns information about a button of type inlineKeyboardButtonTypeLoginUrl. The method needs to be called when the user presses the button
    """

    __type__: Literal["getLoginUrlInfo"] = "getLoginUrlInfo"
    __returning_type__ = LoginUrlInfo

    chat_id: int
    """Chat identifier of the message with the button"""
    message_id: int
    """Message identifier of the message with the button. The message must not be scheduled"""
    button_id: int
    """Button identifier"""

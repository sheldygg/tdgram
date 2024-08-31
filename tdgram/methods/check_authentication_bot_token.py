from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class CheckAuthenticationBotToken(BaseMethod):
    """
    Checks the authentication token of a bot; to log in as a bot. Works only when the current authorization state is authorizationStateWaitPhoneNumber. Can be used instead of setAuthenticationPhoneNumber and checkAuthenticationCode to log in
    """

    __type__: Literal["checkAuthenticationBotToken"] = "checkAuthenticationBotToken"
    __returning_type__ = Ok

    token: str
    """The bot token"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AuthenticationCodeTypeTelegramMessage(BaseType):
    """
    A digit-only authentication code is delivered via a private Telegram message, which can be viewed from another active session
    """

    __type__: Literal["authenticationCodeTypeTelegramMessage"] = (
        "authenticationCodeTypeTelegramMessage"
    )

    length: int
    """Length of the code"""

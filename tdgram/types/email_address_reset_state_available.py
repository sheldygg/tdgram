from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class EmailAddressResetStateAvailable(BaseType):
    """
    Email address can be reset after the given period. Call resetAuthenticationEmailAddress to reset it and allow the user to authorize with a code sent to the user's phone number
    """

    __type__: Literal["emailAddressResetStateAvailable"] = "emailAddressResetStateAvailable"

    wait_period: int
    """Time required to wait before the email address can be reset; 0 if the user is subscribed to Telegram Premium"""

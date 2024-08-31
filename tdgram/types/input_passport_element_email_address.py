from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputPassportElementEmailAddress(BaseType):
    """
    A Telegram Passport element to be saved containing the user's email address
    """

    __type__: Literal["inputPassportElementEmailAddress"] = "inputPassportElementEmailAddress"

    email_address: str
    """The email address to be saved"""

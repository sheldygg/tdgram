from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PassportElementEmailAddress(BaseType):
    """
    A Telegram Passport element containing the user's email address
    """

    __type__: Literal["passportElementEmailAddress"] = "passportElementEmailAddress"

    email_address: str
    """Email address"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PassportElementPhoneNumber(BaseType):
    """
    A Telegram Passport element containing the user's phone number
    """

    __type__: Literal["passportElementPhoneNumber"] = "passportElementPhoneNumber"

    phone_number: str
    """Phone number"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputPassportElementPhoneNumber(BaseType):
    """
    A Telegram Passport element to be saved containing the user's phone number
    """

    __type__: Literal["inputPassportElementPhoneNumber"] = "inputPassportElementPhoneNumber"

    phone_number: str
    """The phone number to be saved"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PassportElementTypePhoneNumber(BaseType):
    """
    A Telegram Passport element containing the user's phone number
    """

    __type__: Literal["passportElementTypePhoneNumber"] = "passportElementTypePhoneNumber"

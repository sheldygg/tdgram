from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PassportElementTypeUtilityBill(BaseType):
    """
    A Telegram Passport element containing the user's utility bill
    """

    __type__: Literal["passportElementTypeUtilityBill"] = "passportElementTypeUtilityBill"

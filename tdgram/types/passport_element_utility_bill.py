from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PersonalDocument


@dataclass(kw_only=True)
class PassportElementUtilityBill(BaseType):
    """
    A Telegram Passport element containing the user's utility bill
    """

    __type__: Literal["passportElementUtilityBill"] = "passportElementUtilityBill"

    utility_bill: PersonalDocument
    """Utility bill"""

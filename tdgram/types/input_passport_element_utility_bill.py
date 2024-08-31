from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputPersonalDocument


@dataclass(kw_only=True)
class InputPassportElementUtilityBill(BaseType):
    """
    A Telegram Passport element to be saved containing the user's utility bill
    """

    __type__: Literal["inputPassportElementUtilityBill"] = "inputPassportElementUtilityBill"

    utility_bill: InputPersonalDocument
    """The utility bill to be saved"""

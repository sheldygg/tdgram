from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BankCardInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class GetBankCardInfo(BaseMethod):
    """
    Returns information about a bank card
    """

    __type__: Literal["getBankCardInfo"] = "getBankCardInfo"
    __returning_type__ = BankCardInfo

    bank_card_number: str
    """The bank card number"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatRevenueAmount(BaseType):
    """
    Contains information about revenue earned from sponsored messages in a chat
    """

    __type__: Literal["chatRevenueAmount"] = "chatRevenueAmount"

    cryptocurrency: str
    """Cryptocurrency in which revenue is calculated"""
    total_amount: int
    """Total amount of the cryptocurrency earned, in the smallest units of the cryptocurrency"""
    balance_amount: int
    """Amount of the cryptocurrency that isn't withdrawn yet, in the smallest units of the cryptocurrency"""
    available_amount: int
    """Amount of the cryptocurrency available for withdrawal, in the smallest units of the cryptocurrency"""
    withdrawal_enabled: bool
    """True, if Telegram Stars can be withdrawn now or later"""

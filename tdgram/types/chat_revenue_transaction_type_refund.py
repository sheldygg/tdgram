from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatRevenueTransactionTypeRefund(BaseType):
    """
    Describes a refund for failed withdrawal of earnings
    """

    __type__: Literal["chatRevenueTransactionTypeRefund"] = "chatRevenueTransactionTypeRefund"

    refund_date: int
    """Point in time (Unix timestamp) when the transaction was refunded"""
    provider: str
    """Name of the payment provider"""

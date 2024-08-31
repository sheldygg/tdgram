from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PaymentReceiptTypeStars(BaseType):
    """
    The payment was done using Telegram Stars
    """

    __type__: Literal["paymentReceiptTypeStars"] = "paymentReceiptTypeStars"

    star_count: int
    """Number of Telegram Stars that were paid"""
    transaction_id: str
    """Unique identifier of the transaction that can be used to dispute it"""

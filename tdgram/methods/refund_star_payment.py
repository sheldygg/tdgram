from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class RefundStarPayment(BaseMethod):
    """
    Refunds a previously done payment in Telegram Stars; for bots only
    """

    __type__: Literal["refundStarPayment"] = "refundStarPayment"
    __returning_type__ = Ok

    user_id: int
    """Identifier of the user that did the payment"""
    telegram_payment_charge_id: str
    """Telegram payment identifier"""

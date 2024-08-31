from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PaymentFormTypeStars(BaseType):
    """
    The payment form is for a payment in Telegram Stars
    """

    __type__: Literal["paymentFormTypeStars"] = "paymentFormTypeStars"

    star_count: int
    """Number of Telegram Stars that will be paid"""

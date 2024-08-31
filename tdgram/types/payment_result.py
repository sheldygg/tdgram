from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PaymentResult(BaseType):
    """
    Contains the result of a payment request
    """

    __type__: Literal["paymentResult"] = "paymentResult"

    success: bool
    """True, if the payment request was successful; otherwise, the verification_url will be non-empty"""
    verification_url: str
    """URL for additional payment credentials verification"""

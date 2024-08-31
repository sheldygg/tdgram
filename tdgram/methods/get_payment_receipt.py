from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import PaymentReceipt
from .base import BaseMethod


@dataclass(kw_only=True)
class GetPaymentReceipt(BaseMethod):
    """
    Returns information about a successful payment
    """

    __type__: Literal["getPaymentReceipt"] = "getPaymentReceipt"
    __returning_type__ = PaymentReceipt

    chat_id: int
    """Chat identifier of the messagePaymentSuccessful message"""
    message_id: int
    """Message identifier"""

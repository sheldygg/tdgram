from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputCredentials, InputInvoice, PaymentResult
from .base import BaseMethod


@dataclass(kw_only=True)
class SendPaymentForm(BaseMethod):
    """
    Sends a filled-out payment form to the bot for final verification
    """

    __type__: Literal["sendPaymentForm"] = "sendPaymentForm"
    __returning_type__ = PaymentResult

    input_invoice: InputInvoice
    """The invoice"""
    payment_form_id: int
    """Payment form identifier returned by getPaymentForm"""
    order_info_id: str
    """Identifier returned by validateOrderInfo, or an empty string"""
    shipping_option_id: str
    """Identifier of a chosen shipping option, if applicable"""
    credentials: InputCredentials | None = None
    """The credentials chosen by user for payment; pass null for a payment in Telegram Stars"""
    tip_amount: int
    """Chosen by the user amount of tip in the smallest units of the currency"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputInvoice, PaymentForm, ThemeParameters
from .base import BaseMethod


@dataclass(kw_only=True)
class GetPaymentForm(BaseMethod):
    """
    Returns an invoice payment form. This method must be called when the user presses inline button of the type inlineKeyboardButtonTypeBuy, or wants to buy access to media in a messagePaidMedia message
    """

    __type__: Literal["getPaymentForm"] = "getPaymentForm"
    __returning_type__ = PaymentForm

    input_invoice: InputInvoice
    """The invoice"""
    theme: ThemeParameters | None = None
    """Preferred payment form theme; pass null to use the default theme"""

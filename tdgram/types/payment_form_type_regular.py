from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Invoice, OrderInfo, PaymentOption, PaymentProvider, SavedCredentials


@dataclass(kw_only=True)
class PaymentFormTypeRegular(BaseType):
    """
    The payment form is for a regular payment
    """

    __type__: Literal["paymentFormTypeRegular"] = "paymentFormTypeRegular"

    invoice: Invoice
    """Full information about the invoice"""
    payment_provider_user_id: int
    """User identifier of the payment provider bot"""
    payment_provider: PaymentProvider
    """Information about the payment provider"""
    additional_payment_options: list[PaymentOption]
    """The list of additional payment options"""
    saved_order_info: OrderInfo | None = None
    """Saved server-side order information; may be null"""
    saved_credentials: list[SavedCredentials]
    """The list of saved payment credentials"""
    can_save_credentials: bool
    """True, if the user can choose to save credentials"""
    need_password: bool
    """True, if the user will be able to save credentials, if sets up a 2-step verification password"""

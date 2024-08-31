from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PaymentProviderStripe(BaseType):
    """
    Stripe payment provider
    """

    __type__: Literal["paymentProviderStripe"] = "paymentProviderStripe"

    publishable_key: str
    """Stripe API publishable key"""
    need_country: bool
    """True, if the user country must be provided"""
    need_postal_code: bool
    """True, if the user ZIP/postal code must be provided"""
    need_cardholder_name: bool
    """True, if the cardholder name must be provided"""

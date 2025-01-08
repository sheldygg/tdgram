from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import StarSubscriptionPricing


@dataclass(kw_only=True)
class PaymentFormTypeStarSubscription(BaseType):
    """
    The payment form is for a payment in Telegram Stars for subscription
    """

    __type__: Literal["paymentFormTypeStarSubscription"] = "paymentFormTypeStarSubscription"

    pricing: StarSubscriptionPricing
    """Information about subscription plan"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StorePaymentPurposePremiumSubscription(BaseType):
    """
    The user subscribing to Telegram Premium
    """

    __type__: Literal["storePaymentPurposePremiumSubscription"] = (
        "storePaymentPurposePremiumSubscription"
    )

    is_restore: bool
    """Pass true if this is a restore of a Telegram Premium purchase; only for App Store"""
    is_upgrade: bool
    """Pass true if this is an upgrade from a monthly subscription to early subscription; only for App Store"""

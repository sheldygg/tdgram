from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PremiumPaymentOption


@dataclass(kw_only=True)
class PremiumStatePaymentOption(BaseType):
    """
    Describes an option for buying or upgrading Telegram Premium for self
    """

    __type__: Literal["premiumStatePaymentOption"] = "premiumStatePaymentOption"

    payment_option: PremiumPaymentOption
    """Information about the payment option"""
    is_current: bool
    """True, if this is the currently used Telegram Premium subscription option"""
    is_upgrade: bool
    """True, if the payment option can be used to upgrade the existing Telegram Premium subscription"""
    last_transaction_id: str
    """Identifier of the last in-store transaction for the currently used option"""

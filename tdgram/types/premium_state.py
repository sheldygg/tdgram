from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import (
        BusinessFeaturePromotionAnimation,
        FormattedText,
        PremiumFeaturePromotionAnimation,
        PremiumStatePaymentOption,
    )


@dataclass(kw_only=True)
class PremiumState(BaseType):
    """
    Contains state of Telegram Premium subscription and promotion videos for Premium features
    """

    __type__: Literal["premiumState"] = "premiumState"

    state: FormattedText | None = None
    """Text description of the state of the current Premium subscription; may be empty if the current user has no Telegram Premium subscription"""
    payment_options: list[PremiumStatePaymentOption]
    """The list of available options for buying Telegram Premium"""
    animations: list[PremiumFeaturePromotionAnimation]
    """The list of available promotion animations for Premium features"""
    business_animations: list[BusinessFeaturePromotionAnimation]
    """The list of available promotion animations for Business features"""

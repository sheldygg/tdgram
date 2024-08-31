from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InternalLinkType, PremiumFeature, PremiumLimit


@dataclass(kw_only=True)
class PremiumFeatures(BaseType):
    """
    Contains information about features, available to Premium users
    """

    __type__: Literal["premiumFeatures"] = "premiumFeatures"

    features: list[PremiumFeature]
    """The list of available features"""
    limits: list[PremiumLimit]
    """The list of limits, increased for Premium users"""
    payment_link: InternalLinkType | None = None
    """An internal link to be opened to pay for Telegram Premium if store payment isn't possible; may be null if direct payment isn't available"""

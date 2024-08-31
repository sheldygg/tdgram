from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Animation, PremiumFeature


@dataclass(kw_only=True)
class PremiumFeaturePromotionAnimation(BaseType):
    """
    Describes a promotion animation for a Premium feature
    """

    __type__: Literal["premiumFeaturePromotionAnimation"] = "premiumFeaturePromotionAnimation"

    feature: PremiumFeature
    """Premium feature"""
    animation: Animation
    """Promotion animation for the feature"""

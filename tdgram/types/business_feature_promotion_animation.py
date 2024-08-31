from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Animation, BusinessFeature


@dataclass(kw_only=True)
class BusinessFeaturePromotionAnimation(BaseType):
    """
    Describes a promotion animation for a Business feature
    """

    __type__: Literal["businessFeaturePromotionAnimation"] = "businessFeaturePromotionAnimation"

    feature: BusinessFeature
    """Business feature"""
    animation: Animation
    """Promotion animation for the feature"""

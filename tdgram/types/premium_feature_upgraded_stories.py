from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumFeatureUpgradedStories(BaseType):
    """
    Allowed to use many additional features for stories
    """

    __type__: Literal["premiumFeatureUpgradedStories"] = "premiumFeatureUpgradedStories"

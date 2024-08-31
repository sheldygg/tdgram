from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumFeatureIncreasedLimits(BaseType):
    """
    Increased limits
    """

    __type__: Literal["premiumFeatureIncreasedLimits"] = "premiumFeatureIncreasedLimits"

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumFeatureAccentColor(BaseType):
    """
    The ability to choose accent color for replies and user profile
    """

    __type__: Literal["premiumFeatureAccentColor"] = "premiumFeatureAccentColor"

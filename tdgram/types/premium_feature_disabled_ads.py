from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumFeatureDisabledAds(BaseType):
    """
    Disabled ads
    """

    __type__: Literal["premiumFeatureDisabledAds"] = "premiumFeatureDisabledAds"

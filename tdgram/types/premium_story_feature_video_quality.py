from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumStoryFeatureVideoQuality(BaseType):
    """
    The ability to choose better quality for viewed stories
    """

    __type__: Literal["premiumStoryFeatureVideoQuality"] = "premiumStoryFeatureVideoQuality"

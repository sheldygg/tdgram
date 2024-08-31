from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumStoryFeatureStealthMode(BaseType):
    """
    The ability to hide the fact that the user viewed other's stories
    """

    __type__: Literal["premiumStoryFeatureStealthMode"] = "premiumStoryFeatureStealthMode"

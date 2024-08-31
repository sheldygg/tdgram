from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumFeatureMessageEffects(BaseType):
    """
    The ability to use all available message effects
    """

    __type__: Literal["premiumFeatureMessageEffects"] = "premiumFeatureMessageEffects"

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumFeatureUniqueStickers(BaseType):
    """
    Allowed to use premium stickers with unique effects
    """

    __type__: Literal["premiumFeatureUniqueStickers"] = "premiumFeatureUniqueStickers"

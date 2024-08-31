from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumFeatureAppIcons(BaseType):
    """
    Allowed to set a premium application icons
    """

    __type__: Literal["premiumFeatureAppIcons"] = "premiumFeatureAppIcons"

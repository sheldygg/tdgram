from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumLimitTypeSavedAnimationCount(BaseType):
    """
    The maximum number of saved animations
    """

    __type__: Literal["premiumLimitTypeSavedAnimationCount"] = (
        "premiumLimitTypeSavedAnimationCount"
    )

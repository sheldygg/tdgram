from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumFeatureBackgroundForBoth(BaseType):
    """
    The ability to set private chat background for both users
    """

    __type__: Literal["premiumFeatureBackgroundForBoth"] = "premiumFeatureBackgroundForBoth"

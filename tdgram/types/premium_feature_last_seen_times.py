from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumFeatureLastSeenTimes(BaseType):
    """
    The ability to view last seen and read times of other users even they can't view last seen or read time for the current user
    """

    __type__: Literal["premiumFeatureLastSeenTimes"] = "premiumFeatureLastSeenTimes"

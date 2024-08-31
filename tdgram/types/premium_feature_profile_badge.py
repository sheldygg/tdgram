from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumFeatureProfileBadge(BaseType):
    """
    A badge in the user's profile
    """

    __type__: Literal["premiumFeatureProfileBadge"] = "premiumFeatureProfileBadge"

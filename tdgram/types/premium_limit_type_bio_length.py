from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumLimitTypeBioLength(BaseType):
    """
    The maximum length of the user's bio
    """

    __type__: Literal["premiumLimitTypeBioLength"] = "premiumLimitTypeBioLength"

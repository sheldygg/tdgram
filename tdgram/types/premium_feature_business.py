from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumFeatureBusiness(BaseType):
    """
    The ability to use Business features
    """

    __type__: Literal["premiumFeatureBusiness"] = "premiumFeatureBusiness"

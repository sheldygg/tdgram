from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumFeatureUniqueReactions(BaseType):
    """
    Allowed to use more reactions
    """

    __type__: Literal["premiumFeatureUniqueReactions"] = "premiumFeatureUniqueReactions"

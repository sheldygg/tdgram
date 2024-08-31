from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumStoryFeaturePriorityOrder(BaseType):
    """
    Stories of the current user are displayed before stories of non-Premium contacts, supergroups, and channels
    """

    __type__: Literal["premiumStoryFeaturePriorityOrder"] = "premiumStoryFeaturePriorityOrder"

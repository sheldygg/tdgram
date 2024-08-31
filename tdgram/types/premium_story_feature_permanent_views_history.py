from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumStoryFeaturePermanentViewsHistory(BaseType):
    """
    The ability to check who opened the current user's stories after they expire
    """

    __type__: Literal["premiumStoryFeaturePermanentViewsHistory"] = (
        "premiumStoryFeaturePermanentViewsHistory"
    )

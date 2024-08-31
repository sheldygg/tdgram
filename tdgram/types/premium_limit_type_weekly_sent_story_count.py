from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumLimitTypeWeeklySentStoryCount(BaseType):
    """
    The maximum number of stories sent per week
    """

    __type__: Literal["premiumLimitTypeWeeklySentStoryCount"] = (
        "premiumLimitTypeWeeklySentStoryCount"
    )

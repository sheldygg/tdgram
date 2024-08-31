from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumLimitTypeStorySuggestedReactionAreaCount(BaseType):
    """
    The maximum number of suggested reaction areas on a story
    """

    __type__: Literal["premiumLimitTypeStorySuggestedReactionAreaCount"] = (
        "premiumLimitTypeStorySuggestedReactionAreaCount"
    )

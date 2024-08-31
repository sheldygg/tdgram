from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumLimitTypeActiveStoryCount(BaseType):
    """
    The maximum number of active stories
    """

    __type__: Literal["premiumLimitTypeActiveStoryCount"] = "premiumLimitTypeActiveStoryCount"

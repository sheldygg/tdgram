from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumStoryFeatureSaveStories(BaseType):
    """
    The ability to save other's unprotected stories
    """

    __type__: Literal["premiumStoryFeatureSaveStories"] = "premiumStoryFeatureSaveStories"

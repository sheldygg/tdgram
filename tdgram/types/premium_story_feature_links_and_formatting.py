from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumStoryFeatureLinksAndFormatting(BaseType):
    """
    The ability to use links and formatting in story caption, and use inputStoryAreaTypeLink areas
    """

    __type__: Literal["premiumStoryFeatureLinksAndFormatting"] = (
        "premiumStoryFeatureLinksAndFormatting"
    )

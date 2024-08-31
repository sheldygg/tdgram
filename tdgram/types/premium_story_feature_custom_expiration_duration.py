from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumStoryFeatureCustomExpirationDuration(BaseType):
    """
    The ability to set custom expiration duration for stories
    """

    __type__: Literal["premiumStoryFeatureCustomExpirationDuration"] = (
        "premiumStoryFeatureCustomExpirationDuration"
    )

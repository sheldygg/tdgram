from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumFeatureRealTimeChatTranslation(BaseType):
    """
    Allowed to translate chat messages real-time
    """

    __type__: Literal["premiumFeatureRealTimeChatTranslation"] = (
        "premiumFeatureRealTimeChatTranslation"
    )

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumFeatureCustomEmoji(BaseType):
    """
    Allowed to use custom emoji stickers in message texts and captions
    """

    __type__: Literal["premiumFeatureCustomEmoji"] = "premiumFeatureCustomEmoji"

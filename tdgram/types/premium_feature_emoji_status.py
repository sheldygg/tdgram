from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumFeatureEmojiStatus(BaseType):
    """
    The ability to show an emoji status along with the user's name
    """

    __type__: Literal["premiumFeatureEmojiStatus"] = "premiumFeatureEmojiStatus"

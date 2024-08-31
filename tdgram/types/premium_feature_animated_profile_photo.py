from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumFeatureAnimatedProfilePhoto(BaseType):
    """
    Profile photo animation on message and chat screens
    """

    __type__: Literal["premiumFeatureAnimatedProfilePhoto"] = "premiumFeatureAnimatedProfilePhoto"

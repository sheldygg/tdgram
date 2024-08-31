from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumFeatureSavedMessagesTags(BaseType):
    """
    The ability to use tags in Saved Messages
    """

    __type__: Literal["premiumFeatureSavedMessagesTags"] = "premiumFeatureSavedMessagesTags"

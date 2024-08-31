from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumFeatureChatBoost(BaseType):
    """
    The ability to boost chats
    """

    __type__: Literal["premiumFeatureChatBoost"] = "premiumFeatureChatBoost"

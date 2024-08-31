from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumLimitTypePinnedChatCount(BaseType):
    """
    The maximum number of pinned chats in the main chat list
    """

    __type__: Literal["premiumLimitTypePinnedChatCount"] = "premiumLimitTypePinnedChatCount"

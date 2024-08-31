from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumLimitTypePinnedSavedMessagesTopicCount(BaseType):
    """
    The maximum number of pinned Saved Messages topics
    """

    __type__: Literal["premiumLimitTypePinnedSavedMessagesTopicCount"] = (
        "premiumLimitTypePinnedSavedMessagesTopicCount"
    )

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SuggestedActionExtendStarSubscriptions(BaseType):
    """
    Suggests the user to extend their expiring Telegram Star subscriptions. Call getStarSubscriptions with only_expiring == true
    """

    __type__: Literal["suggestedActionExtendStarSubscriptions"] = (
        "suggestedActionExtendStarSubscriptions"
    )

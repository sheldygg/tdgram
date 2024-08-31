from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SuggestedActionExtendPremium(BaseType):
    """
    Suggests the user to extend their expiring Telegram Premium subscription
    """

    __type__: Literal["suggestedActionExtendPremium"] = "suggestedActionExtendPremium"

    manage_premium_subscription_url: str
    """A URL for managing Telegram Premium subscription"""

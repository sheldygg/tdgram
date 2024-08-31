from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SuggestedActionGiftPremiumForChristmas(BaseType):
    """
    Suggests the user to gift Telegram Premium to friends for Christmas
    """

    __type__: Literal["suggestedActionGiftPremiumForChristmas"] = (
        "suggestedActionGiftPremiumForChristmas"
    )

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CanSendStoryResultMonthlyLimitExceeded(BaseType):
    """
    The monthly limit for the number of posted stories exceeded. The user needs to buy Telegram Premium or wait specified time
    """

    __type__: Literal["canSendStoryResultMonthlyLimitExceeded"] = (
        "canSendStoryResultMonthlyLimitExceeded"
    )

    retry_after: int
    """Time left before the user can send the next story"""

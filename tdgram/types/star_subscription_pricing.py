from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StarSubscriptionPricing(BaseType):
    """
    Describes subscription plan paid in Telegram Stars
    """

    __type__: Literal["starSubscriptionPricing"] = "starSubscriptionPricing"

    period: int
    """The number of seconds between consecutive Telegram Star debiting"""
    star_count: int
    """The amount of Telegram Stars that must be paid for each period"""

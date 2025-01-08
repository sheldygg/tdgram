from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PushMessageContentGift(BaseType):
    """
    A message with a gift
    """

    __type__: Literal["pushMessageContentGift"] = "pushMessageContentGift"

    star_count: int
    """Number of Telegram Stars that sender paid for the gift"""

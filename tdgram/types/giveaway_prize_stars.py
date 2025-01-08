from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class GiveawayPrizeStars(BaseType):
    """
    The giveaway sends Telegram Stars to the winners
    """

    __type__: Literal["giveawayPrizeStars"] = "giveawayPrizeStars"

    star_count: int
    """Number of Telegram Stars that will be shared by all winners"""

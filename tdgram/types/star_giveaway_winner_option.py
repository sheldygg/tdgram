from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StarGiveawayWinnerOption(BaseType):
    """
    Describes an option for the number of winners of a Telegram Star giveaway
    """

    __type__: Literal["starGiveawayWinnerOption"] = "starGiveawayWinnerOption"

    winner_count: int
    """The number of users that will be chosen as winners"""
    won_star_count: int
    """The number of Telegram Stars that will be won by the winners of the giveaway"""
    is_default: bool
    """True, if the option must be chosen by default"""

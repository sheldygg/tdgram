from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import GiveawayParameters, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class LaunchPrepaidGiveaway(BaseMethod):
    """
    Launches a prepaid giveaway
    """

    __type__: Literal["launchPrepaidGiveaway"] = "launchPrepaidGiveaway"
    __returning_type__ = Ok

    giveaway_id: int
    """Unique identifier of the prepaid giveaway"""
    parameters: GiveawayParameters
    """Giveaway parameters"""
    winner_count: int
    """The number of users to receive giveaway prize"""
    star_count: int
    """The number of Telegram Stars to be distributed through the giveaway; pass 0 for Telegram Premium giveaways"""

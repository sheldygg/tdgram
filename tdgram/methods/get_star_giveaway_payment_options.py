from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import StarGiveawayPaymentOptions
from .base import BaseMethod


@dataclass(kw_only=True)
class GetStarGiveawayPaymentOptions(BaseMethod):
    """
    Returns available options for Telegram Star giveaway creation
    """

    __type__: Literal["getStarGiveawayPaymentOptions"] = "getStarGiveawayPaymentOptions"
    __returning_type__ = StarGiveawayPaymentOptions

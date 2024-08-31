from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import PremiumGiveawayInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class GetPremiumGiveawayInfo(BaseMethod):
    """
    Returns information about a Telegram Premium giveaway
    """

    __type__: Literal["getPremiumGiveawayInfo"] = "getPremiumGiveawayInfo"
    __returning_type__ = PremiumGiveawayInfo

    chat_id: int
    """Identifier of the channel chat which started the giveaway"""
    message_id: int
    """Identifier of the giveaway or a giveaway winners message in the chat"""

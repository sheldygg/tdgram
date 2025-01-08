from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import GiveawayInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class GetGiveawayInfo(BaseMethod):
    """
    Returns information about a giveaway
    """

    __type__: Literal["getGiveawayInfo"] = "getGiveawayInfo"
    __returning_type__ = GiveawayInfo

    chat_id: int
    """Identifier of the channel chat which started the giveaway"""
    message_id: int
    """Identifier of the giveaway or a giveaway winners message in the chat"""

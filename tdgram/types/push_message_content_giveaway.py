from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import GiveawayPrize


@dataclass(kw_only=True)
class PushMessageContentGiveaway(BaseType):
    """
    A message with a giveaway
    """

    __type__: Literal["pushMessageContentGiveaway"] = "pushMessageContentGiveaway"

    winner_count: int
    """Number of users which will receive giveaway prizes; 0 for pinned message"""
    prize: GiveawayPrize | None = None
    """Prize of the giveaway; may be null for pinned message"""
    is_pinned: bool
    """True, if the message is a pinned message with the specified content"""

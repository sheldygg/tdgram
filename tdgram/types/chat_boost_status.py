from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PrepaidPremiumGiveaway


@dataclass(kw_only=True)
class ChatBoostStatus(BaseType):
    """
    Describes current boost status of a chat
    """

    __type__: Literal["chatBoostStatus"] = "chatBoostStatus"

    boost_url: str
    """An HTTP URL, which can be used to boost the chat"""
    applied_slot_ids: list[int]
    """Identifiers of boost slots of the current user applied to the chat"""
    level: int
    """Current boost level of the chat"""
    gift_code_boost_count: int
    """The number of boosts received by the chat from created Telegram Premium gift codes and giveaways; always 0 if the current user isn't an administrator in the chat"""
    boost_count: int
    """The number of boosts received by the chat"""
    current_level_boost_count: int
    """The number of boosts added to reach the current level"""
    next_level_boost_count: int
    """The number of boosts needed to reach the next level; 0 if the next level isn't available"""
    premium_member_count: int
    """Approximate number of Telegram Premium subscribers joined the chat; always 0 if the current user isn't an administrator in the chat"""
    premium_member_percentage: float
    """A percentage of Telegram Premium subscribers joined the chat; always 0 if the current user isn't an administrator in the chat"""
    prepaid_giveaways: list[PrepaidPremiumGiveaway]
    """The list of prepaid giveaways available for the chat; only for chat administrators"""

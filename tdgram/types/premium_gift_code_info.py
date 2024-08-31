from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageSender


@dataclass(kw_only=True)
class PremiumGiftCodeInfo(BaseType):
    """
    Contains information about a Telegram Premium gift code
    """

    __type__: Literal["premiumGiftCodeInfo"] = "premiumGiftCodeInfo"

    creator_id: MessageSender | None = None
    """Identifier of a chat or a user that created the gift code; may be null if unknown. If null and the code is from messagePremiumGiftCode message, then creator_id from the message can be used"""
    creation_date: int
    """Point in time (Unix timestamp) when the code was created"""
    is_from_giveaway: bool
    """True, if the gift code was created for a giveaway"""
    giveaway_message_id: int
    """Identifier of the corresponding giveaway message in the creator_id chat; can be 0 or an identifier of a deleted message"""
    month_count: int
    """Number of months the Telegram Premium subscription will be active after code activation"""
    user_id: int
    """Identifier of a user for which the code was created; 0 if none"""
    use_date: int
    """Point in time (Unix timestamp) when the code was activated; 0 if none"""

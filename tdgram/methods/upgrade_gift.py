from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import UpgradeGiftResult
from .base import BaseMethod


@dataclass(kw_only=True)
class UpgradeGift(BaseMethod):
    """
    Upgrades a gift received by the current user. Unless the gift has prepaid_upgrade_star_count > 0, the user must pay gift.upgrade_star_count Telegram Stars for the upgrade
    """

    __type__: Literal["upgradeGift"] = "upgradeGift"
    __returning_type__ = UpgradeGiftResult

    sender_user_id: int
    """Identifier of the user that sent the gift"""
    message_id: int
    """Identifier of the message with the gift in the chat with the user"""
    keep_original_details: bool
    """Pass true to keep the original gift text, sender and receiver in the upgraded gift"""

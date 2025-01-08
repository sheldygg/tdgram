from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import UpgradedGift


@dataclass(kw_only=True)
class UpgradeGiftResult(BaseType):
    """
    Contains result of gift upgrading
    """

    __type__: Literal["upgradeGiftResult"] = "upgradeGiftResult"

    gift: UpgradedGift
    """The upgraded gift"""
    is_saved: bool
    """True, if the gift is displayed on the user's profile page"""
    can_be_transferred: bool
    """True, if the gift can be transferred to another user"""
    transfer_star_count: int
    """Number of Telegram Stars that must be paid to transfer the upgraded gift"""
    export_date: int
    """Point in time (Unix timestamp) when the gift can be transferred to TON blockchain as an NFT"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import UpgradedGift


@dataclass(kw_only=True)
class MessageUpgradedGift(BaseType):
    """
    An upgraded gift was received or sent by the current user
    """

    __type__: Literal["messageUpgradedGift"] = "messageUpgradedGift"

    gift: UpgradedGift
    """The gift"""
    is_upgrade: bool
    """True, if the gift was obtained by upgrading of a previously received gift; otherwise, this is a transferred gift"""
    is_saved: bool
    """True, if the gift is displayed on the user's profile page; only for the receiver of the gift"""
    can_be_transferred: bool
    """True, if the gift can be transferred to another user; only for the receiver of the gift"""
    was_transferred: bool
    """True, if the gift was transferred to another user; only for the receiver of the gift"""
    transfer_star_count: int
    """Number of Telegram Stars that must be paid to transfer the upgraded gift; only for the receiver of the gift"""
    export_date: int
    """Point in time (Unix timestamp) when the gift can be transferred to TON blockchain as an NFT; 0 if NFT export isn't possible; only for the receiver of the gift"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText, Gift


@dataclass(kw_only=True)
class MessageGift(BaseType):
    """
    A regular gift was received or sent by the current user
    """

    __type__: Literal["messageGift"] = "messageGift"

    gift: Gift
    """The gift"""
    text: FormattedText
    """Message added to the gift"""
    sell_star_count: int
    """Number of Telegram Stars that can be claimed by the receiver instead of the regular gift; 0 if the gift can't be sold by the receiver"""
    prepaid_upgrade_star_count: int
    """Number of Telegram Stars that were paid by the sender for the ability to upgrade the gift"""
    is_private: bool
    """True, if the sender and gift text are shown only to the gift receiver; otherwise, everyone will be able to see them"""
    is_saved: bool
    """True, if the gift is displayed on the user's profile page; only for the receiver of the gift"""
    can_be_upgraded: bool
    """True, if the gift can be upgraded to a unique gift; only for the receiver of the gift"""
    was_converted: bool
    """True, if the gift was converted to Telegram Stars; only for the receiver of the gift"""
    was_upgraded: bool
    """True, if the gift was upgraded to a unique gift"""
    was_refunded: bool
    """True, if the gift was refunded and isn't available anymore"""
    upgrade_message_id: int
    """Identifier of the service message messageUpgradedGift or messageRefundedUpgradedGift with upgraded version of the gift; can be 0 if none or an identifier of a deleted message."""

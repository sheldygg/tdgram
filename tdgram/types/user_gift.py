from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText, SentGift


@dataclass(kw_only=True)
class UserGift(BaseType):
    """
    Represents a gift received by a user
    """

    __type__: Literal["userGift"] = "userGift"

    sender_user_id: int
    """Identifier of the user that sent the gift; 0 if unknown"""
    text: FormattedText
    """Message added to the gift"""
    is_private: bool
    """True, if the sender and gift text are shown only to the gift receiver; otherwise, everyone are able to see them"""
    is_saved: bool
    """True, if the gift is displayed on the user's profile page; only for the receiver of the gift"""
    can_be_upgraded: bool
    """True, if the gift is a regular gift that can be upgraded to a unique gift; only for the receiver of the gift"""
    can_be_transferred: bool
    """True, if the gift is an upgraded gift that can be transferred to another user; only for the receiver of the gift"""
    was_refunded: bool
    """True, if the gift was refunded and isn't available anymore"""
    date: int
    """Point in time (Unix timestamp) when the gift was sent"""
    gift: SentGift
    """The gift"""
    message_id: int
    """Identifier of the message with the gift in the chat with the sender of the gift; can be 0 or an identifier of a deleted message; only for the receiver of the gift"""
    sell_star_count: int
    """Number of Telegram Stars that can be claimed by the receiver instead of the regular gift; 0 if the gift can't be sold by the current user"""
    prepaid_upgrade_star_count: int
    """Number of Telegram Stars that were paid by the sender for the ability to upgrade the gift"""
    transfer_star_count: int
    """Number of Telegram Stars that must be paid to transfer the upgraded gift; only for the receiver of the gift"""
    export_date: int
    """Point in time (Unix timestamp) when the upgraded gift can be transferred to TON blockchain as an NFT; 0 if NFT export isn't possible; only for the receiver of the gift"""

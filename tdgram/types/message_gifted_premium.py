from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Sticker


@dataclass(kw_only=True)
class MessageGiftedPremium(BaseType):
    """
    Telegram Premium was gifted to a user
    """

    __type__: Literal["messageGiftedPremium"] = "messageGiftedPremium"

    gifter_user_id: int
    """The identifier of a user that gifted Telegram Premium; 0 if the gift was anonymous or is outgoing"""
    receiver_user_id: int
    """The identifier of a user that received Telegram Premium; 0 if the gift is incoming"""
    currency: str
    """Currency for the paid amount"""
    amount: int
    """The paid amount, in the smallest units of the currency"""
    cryptocurrency: str | None = None
    """Cryptocurrency used to pay for the gift; may be empty if none"""
    cryptocurrency_amount: int
    """The paid amount, in the smallest units of the cryptocurrency; 0 if none"""
    month_count: int
    """Number of months the Telegram Premium subscription will be active"""
    sticker: Sticker | None = None
    """A sticker to be shown in the message; may be null if unknown"""

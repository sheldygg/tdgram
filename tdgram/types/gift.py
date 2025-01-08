from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Sticker


@dataclass(kw_only=True)
class Gift(BaseType):
    """
    Describes a gift that can be sent to another user
    """

    __type__: Literal["gift"] = "gift"

    id: int
    """Unique identifier of the gift"""
    sticker: Sticker
    """The sticker representing the gift"""
    star_count: int
    """Number of Telegram Stars that must be paid for the gift"""
    default_sell_star_count: int
    """Number of Telegram Stars that can be claimed by the receiver instead of the regular gift by default. If the gift was paid with just bought Telegram Stars, then full value can be claimed"""
    upgrade_star_count: int
    """Number of Telegram Stars that must be paid to upgrade the gift; 0 if upgrade isn't possible"""
    is_for_birthday: bool
    """True, if the gift is a birthday gift"""
    remaining_count: int
    """Number of remaining times the gift can be purchased by all users; 0 if not limited or the gift was sold out"""
    total_count: int
    """Number of total times the gift can be purchased by all users; 0 if not limited"""
    first_send_date: int
    """Point in time (Unix timestamp) when the gift was send for the first time; for sold out gifts only"""
    last_send_date: int
    """Point in time (Unix timestamp) when the gift was send for the last time; for sold out gifts only"""

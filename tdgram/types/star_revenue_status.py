from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import StarAmount


@dataclass(kw_only=True)
class StarRevenueStatus(BaseType):
    """
    Contains information about Telegram Stars earned by a bot or a chat
    """

    __type__: Literal["starRevenueStatus"] = "starRevenueStatus"

    total_amount: StarAmount
    """Total amount of Telegram Stars earned"""
    current_amount: StarAmount
    """The amount of Telegram Stars that aren't withdrawn yet"""
    available_amount: StarAmount
    """The amount of Telegram Stars that are available for withdrawal"""
    withdrawal_enabled: bool
    """True, if Telegram Stars can be withdrawn now or later"""
    next_withdrawal_in: int
    """Time left before the next withdrawal can be started, in seconds; 0 if withdrawal can be started now"""

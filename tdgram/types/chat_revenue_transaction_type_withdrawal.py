from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import RevenueWithdrawalState


@dataclass(kw_only=True)
class ChatRevenueTransactionTypeWithdrawal(BaseType):
    """
    Describes a withdrawal of earnings
    """

    __type__: Literal["chatRevenueTransactionTypeWithdrawal"] = (
        "chatRevenueTransactionTypeWithdrawal"
    )

    withdrawal_date: int
    """Point in time (Unix timestamp) when the earnings withdrawal started"""
    provider: str
    """Name of the payment provider"""
    state: RevenueWithdrawalState
    """State of the withdrawal"""

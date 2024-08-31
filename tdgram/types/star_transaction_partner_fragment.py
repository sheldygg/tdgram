from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import RevenueWithdrawalState


@dataclass(kw_only=True)
class StarTransactionPartnerFragment(BaseType):
    """
    The transaction is a transaction with Fragment
    """

    __type__: Literal["starTransactionPartnerFragment"] = "starTransactionPartnerFragment"

    withdrawal_state: RevenueWithdrawalState | None = None
    """State of the withdrawal; may be null for refunds from Fragment"""

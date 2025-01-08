from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import RevenueWithdrawalState


@dataclass(kw_only=True)
class StarTransactionTypeFragmentWithdrawal(BaseType):
    """
    The transaction is a withdrawal of earned Telegram Stars to Fragment; for bots and channel chats only
    """

    __type__: Literal["starTransactionTypeFragmentWithdrawal"] = (
        "starTransactionTypeFragmentWithdrawal"
    )

    withdrawal_state: RevenueWithdrawalState | None = None
    """State of the withdrawal; may be null for refunds from Fragment"""

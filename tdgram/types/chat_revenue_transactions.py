from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatRevenueTransaction


@dataclass(kw_only=True)
class ChatRevenueTransactions(BaseType):
    """
    Contains a list of chat revenue transactions
    """

    __type__: Literal["chatRevenueTransactions"] = "chatRevenueTransactions"

    total_count: int
    """Total number of transactions"""
    transactions: list[ChatRevenueTransaction]
    """List of transactions"""

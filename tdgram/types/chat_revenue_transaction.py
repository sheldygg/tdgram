from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatRevenueTransactionType


@dataclass(kw_only=True)
class ChatRevenueTransaction(BaseType):
    """
    Contains a chat revenue transactions
    """

    __type__: Literal["chatRevenueTransaction"] = "chatRevenueTransaction"

    cryptocurrency: str
    """Cryptocurrency in which revenue is calculated"""
    cryptocurrency_amount: int
    """The withdrawn amount, in the smallest units of the cryptocurrency"""
    type: ChatRevenueTransactionType
    """Type of the transaction"""

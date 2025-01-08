from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import StarAmount, StarTransactionType


@dataclass(kw_only=True)
class StarTransaction(BaseType):
    """
    Represents a transaction changing the amount of owned Telegram Stars
    """

    __type__: Literal["starTransaction"] = "starTransaction"

    id: str
    """Unique identifier of the transaction"""
    star_amount: StarAmount
    """The amount of added owned Telegram Stars; negative for outgoing transactions"""
    is_refund: bool
    """True, if the transaction is a refund of a previous transaction"""
    date: int
    """Point in time (Unix timestamp) when the transaction was completed"""
    type: StarTransactionType
    """Type of the transaction"""

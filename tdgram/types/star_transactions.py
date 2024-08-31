from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import StarTransaction


@dataclass(kw_only=True)
class StarTransactions(BaseType):
    """
    Represents a list of Telegram Star transactions
    """

    __type__: Literal["starTransactions"] = "starTransactions"

    star_count: int
    """The amount of owned Telegram Stars"""
    transactions: list[StarTransaction]
    """List of transactions with Telegram Stars"""
    next_offset: str
    """The offset for the next request. If empty, then there are no more results"""

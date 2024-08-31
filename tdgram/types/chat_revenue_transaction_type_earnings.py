from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatRevenueTransactionTypeEarnings(BaseType):
    """
    Describes earnings from sponsored messages in a chat in some time frame
    """

    __type__: Literal["chatRevenueTransactionTypeEarnings"] = "chatRevenueTransactionTypeEarnings"

    start_date: int
    """Point in time (Unix timestamp) when the earnings started"""
    end_date: int
    """Point in time (Unix timestamp) when the earnings ended"""

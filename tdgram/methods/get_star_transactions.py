from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MessageSender, StarTransactionDirection, StarTransactions
from .base import BaseMethod


@dataclass(kw_only=True)
class GetStarTransactions(BaseMethod):
    """
    Returns the list of Telegram Star transactions for the specified owner
    """

    __type__: Literal["getStarTransactions"] = "getStarTransactions"
    __returning_type__ = StarTransactions

    owner_id: MessageSender
    """Identifier of the owner of the Telegram Stars; can be the identifier of the current user, identifier of an owned bot,"""
    subscription_id: str | None = None
    """If non-empty, only transactions related to the Star Subscription will be returned"""
    direction: StarTransactionDirection | None = None
    """Direction of the transactions to receive; pass null to get all transactions"""
    offset: str
    """Offset of the first transaction to return as received from the previous request; use empty string to get the first chunk of results"""
    limit: int
    """The maximum number of transactions to return"""

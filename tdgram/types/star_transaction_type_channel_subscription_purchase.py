from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StarTransactionTypeChannelSubscriptionPurchase(BaseType):
    """
    The transaction is a purchase of a subscription to a channel chat by the current user; for regular users only
    """

    __type__: Literal["starTransactionTypeChannelSubscriptionPurchase"] = (
        "starTransactionTypeChannelSubscriptionPurchase"
    )

    chat_id: int
    """Identifier of the channel chat that created the subscription"""
    subscription_period: int
    """The number of seconds between consecutive Telegram Star debitings"""

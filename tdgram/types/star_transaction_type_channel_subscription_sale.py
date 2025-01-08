from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StarTransactionTypeChannelSubscriptionSale(BaseType):
    """
    The transaction is a sale of a subscription by the channel chat; for channel chats only
    """

    __type__: Literal["starTransactionTypeChannelSubscriptionSale"] = (
        "starTransactionTypeChannelSubscriptionSale"
    )

    user_id: int
    """Identifier of the user that bought the subscription"""
    subscription_period: int
    """The number of seconds between consecutive Telegram Star debitings"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StarTransactionTypeTelegramAdsWithdrawal(BaseType):
    """
    The transaction is a withdrawal of earned Telegram Stars to Telegram Ad platform; for bots and channel chats only
    """

    __type__: Literal["starTransactionTypeTelegramAdsWithdrawal"] = (
        "starTransactionTypeTelegramAdsWithdrawal"
    )

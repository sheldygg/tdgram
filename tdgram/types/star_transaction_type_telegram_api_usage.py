from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StarTransactionTypeTelegramApiUsage(BaseType):
    """
    The transaction is a payment for Telegram API usage; for bots only
    """

    __type__: Literal["starTransactionTypeTelegramApiUsage"] = (
        "starTransactionTypeTelegramApiUsage"
    )

    request_count: int
    """The number of billed requests"""

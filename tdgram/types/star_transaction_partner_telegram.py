from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StarTransactionPartnerTelegram(BaseType):
    """
    The transaction is a transaction with Telegram through a bot
    """

    __type__: Literal["starTransactionPartnerTelegram"] = "starTransactionPartnerTelegram"

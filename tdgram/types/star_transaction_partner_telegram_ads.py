from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StarTransactionPartnerTelegramAds(BaseType):
    """
    The transaction is a transaction with Telegram Ad platform
    """

    __type__: Literal["starTransactionPartnerTelegramAds"] = "starTransactionPartnerTelegramAds"

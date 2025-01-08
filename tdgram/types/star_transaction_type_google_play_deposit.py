from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StarTransactionTypeGooglePlayDeposit(BaseType):
    """
    The transaction is a deposit of Telegram Stars from Google Play; for regular users only
    """

    __type__: Literal["starTransactionTypeGooglePlayDeposit"] = (
        "starTransactionTypeGooglePlayDeposit"
    )

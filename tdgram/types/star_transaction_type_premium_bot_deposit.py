from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StarTransactionTypePremiumBotDeposit(BaseType):
    """
    The transaction is a deposit of Telegram Stars from the Premium bot; for regular users only
    """

    __type__: Literal["starTransactionTypePremiumBotDeposit"] = (
        "starTransactionTypePremiumBotDeposit"
    )

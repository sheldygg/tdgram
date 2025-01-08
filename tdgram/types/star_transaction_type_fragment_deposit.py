from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StarTransactionTypeFragmentDeposit(BaseType):
    """
    The transaction is a deposit of Telegram Stars from Fragment; for regular users and bots only
    """

    __type__: Literal["starTransactionTypeFragmentDeposit"] = "starTransactionTypeFragmentDeposit"

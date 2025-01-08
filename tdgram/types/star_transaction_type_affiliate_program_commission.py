from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StarTransactionTypeAffiliateProgramCommission(BaseType):
    """
    The transaction is a receiving of a commission from an affiliate program; for regular users, bots and channel chats only
    """

    __type__: Literal["starTransactionTypeAffiliateProgramCommission"] = (
        "starTransactionTypeAffiliateProgramCommission"
    )

    chat_id: int
    """Identifier of the chat that created the affiliate program"""
    commission_per_mille: int
    """The number of Telegram Stars received by the affiliate for each 1000 Telegram Stars received by the program owner"""

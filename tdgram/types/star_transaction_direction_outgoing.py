from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StarTransactionDirectionOutgoing(BaseType):
    """
    The transaction is outgoing and decreases the number of owned Telegram Stars
    """

    __type__: Literal["starTransactionDirectionOutgoing"] = "starTransactionDirectionOutgoing"

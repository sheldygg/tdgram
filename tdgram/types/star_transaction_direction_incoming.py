from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StarTransactionDirectionIncoming(BaseType):
    """
    The transaction is incoming and increases the number of owned Telegram Stars
    """

    __type__: Literal["starTransactionDirectionIncoming"] = "starTransactionDirectionIncoming"

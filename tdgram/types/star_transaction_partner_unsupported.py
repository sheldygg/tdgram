from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StarTransactionPartnerUnsupported(BaseType):
    """
    The transaction is a transaction with unknown partner
    """

    __type__: Literal["starTransactionPartnerUnsupported"] = "starTransactionPartnerUnsupported"

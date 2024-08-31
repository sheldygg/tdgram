from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StarTransactionPartnerAppStore(BaseType):
    """
    The transaction is a transaction with App Store
    """

    __type__: Literal["starTransactionPartnerAppStore"] = "starTransactionPartnerAppStore"

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StarTransactionPartnerGooglePlay(BaseType):
    """
    The transaction is a transaction with Google Play
    """

    __type__: Literal["starTransactionPartnerGooglePlay"] = "starTransactionPartnerGooglePlay"

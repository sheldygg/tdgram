from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StarTransactionTypeUnsupported(BaseType):
    """
    The transaction is a transaction of an unsupported type
    """

    __type__: Literal["starTransactionTypeUnsupported"] = "starTransactionTypeUnsupported"

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class RevenueWithdrawalStateFailed(BaseType):
    """
    Withdrawal failed
    """

    __type__: Literal["revenueWithdrawalStateFailed"] = "revenueWithdrawalStateFailed"

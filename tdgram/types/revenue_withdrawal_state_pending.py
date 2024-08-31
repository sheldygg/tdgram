from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class RevenueWithdrawalStatePending(BaseType):
    """
    Withdrawal is pending
    """

    __type__: Literal["revenueWithdrawalStatePending"] = "revenueWithdrawalStatePending"

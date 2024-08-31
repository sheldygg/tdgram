from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class RevenueWithdrawalStateSucceeded(BaseType):
    """
    Withdrawal succeeded
    """

    __type__: Literal["revenueWithdrawalStateSucceeded"] = "revenueWithdrawalStateSucceeded"

    date: int
    """Point in time (Unix timestamp) when the withdrawal was completed"""
    url: str
    """The URL where the withdrawal transaction can be viewed"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PushMessageContentRecurringPayment(BaseType):
    """
    A new recurring payment was made by the current user
    """

    __type__: Literal["pushMessageContentRecurringPayment"] = "pushMessageContentRecurringPayment"

    amount: str
    """The paid amount"""

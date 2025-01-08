from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AccountTtl(BaseType):
    """
    Contains information about the period of inactivity after which the current user's account will automatically be deleted
    """

    __type__: Literal["accountTtl"] = "accountTtl"

    days: int
    """Number of days of inactivity before the account will be flagged for deletion; 30-730 days"""

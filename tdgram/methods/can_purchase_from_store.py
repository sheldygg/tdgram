from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, StorePaymentPurpose
from .base import BaseMethod


@dataclass(kw_only=True)
class CanPurchaseFromStore(BaseMethod):
    """
    Checks whether an in-store purchase is possible. Must be called before any in-store purchase
    """

    __type__: Literal["canPurchaseFromStore"] = "canPurchaseFromStore"
    __returning_type__ = Ok

    purpose: StorePaymentPurpose
    """Transaction purpose"""

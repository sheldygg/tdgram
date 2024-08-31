from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, StorePaymentPurpose
from .base import BaseMethod


@dataclass(kw_only=True)
class AssignAppStoreTransaction(BaseMethod):
    """
    Informs server about a purchase through App Store. For official applications only
    """

    __type__: Literal["assignAppStoreTransaction"] = "assignAppStoreTransaction"
    __returning_type__ = Ok

    receipt: bytes
    """App Store receipt"""
    purpose: StorePaymentPurpose
    """Transaction purpose"""

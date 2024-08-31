from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, StorePaymentPurpose
from .base import BaseMethod


@dataclass(kw_only=True)
class AssignGooglePlayTransaction(BaseMethod):
    """
    Informs server about a purchase through Google Play. For official applications only
    """

    __type__: Literal["assignGooglePlayTransaction"] = "assignGooglePlayTransaction"
    __returning_type__ = Ok

    package_name: str
    """Application package name"""
    store_product_id: str
    """Identifier of the purchased store product"""
    purchase_token: str
    """Google Play purchase token"""
    purpose: StorePaymentPurpose
    """Transaction purpose"""

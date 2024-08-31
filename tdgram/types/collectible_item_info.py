from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CollectibleItemInfo(BaseType):
    """
    Contains information about a collectible item and its last purchase
    """

    __type__: Literal["collectibleItemInfo"] = "collectibleItemInfo"

    purchase_date: int
    """Point in time (Unix timestamp) when the item was purchased"""
    currency: str
    """Currency for the paid amount"""
    amount: int
    """The paid amount, in the smallest units of the currency"""
    cryptocurrency: str
    """Cryptocurrency used to pay for the item"""
    cryptocurrency_amount: int
    """The paid amount, in the smallest units of the cryptocurrency"""
    url: str
    """Individual URL for the item on https://fragment.com"""

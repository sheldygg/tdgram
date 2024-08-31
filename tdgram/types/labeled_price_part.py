from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class LabeledPricePart(BaseType):
    """
    Portion of the price of a product (e.g., 'delivery cost', 'tax amount')
    """

    __type__: Literal["labeledPricePart"] = "labeledPricePart"

    label: str
    """Label for this portion of the product price"""
    amount: int
    """Currency amount in the smallest units of the currency"""

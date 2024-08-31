from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import LabeledPricePart


@dataclass(kw_only=True)
class ShippingOption(BaseType):
    """
    One shipping option
    """

    __type__: Literal["shippingOption"] = "shippingOption"

    id: str
    """Shipping option identifier"""
    title: str
    """Option title"""
    price_parts: list[LabeledPricePart]
    """A list of objects used to calculate the total shipping costs"""

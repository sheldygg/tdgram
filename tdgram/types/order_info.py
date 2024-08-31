from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Address


@dataclass(kw_only=True)
class OrderInfo(BaseType):
    """
    Order information
    """

    __type__: Literal["orderInfo"] = "orderInfo"

    name: str
    """Name of the user"""
    phone_number: str
    """Phone number of the user"""
    email_address: str
    """Email address of the user"""
    shipping_address: Address | None = None
    """Shipping address for this order; may be null"""

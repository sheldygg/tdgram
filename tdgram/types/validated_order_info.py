from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ShippingOption


@dataclass(kw_only=True)
class ValidatedOrderInfo(BaseType):
    """
    Contains a temporary identifier of validated order information, which is stored for one hour, and the available shipping options
    """

    __type__: Literal["validatedOrderInfo"] = "validatedOrderInfo"

    order_info_id: str
    """Temporary identifier of the order information"""
    shipping_options: list[ShippingOption]
    """Available shipping options"""

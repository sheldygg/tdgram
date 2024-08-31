from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import OrderInfo


@dataclass(kw_only=True)
class UpdateNewPreCheckoutQuery(BaseType):
    """
    A new incoming pre-checkout query; for bots only. Contains full information about a checkout
    """

    __type__: Literal["updateNewPreCheckoutQuery"] = "updateNewPreCheckoutQuery"

    id: int
    """Unique query identifier"""
    sender_user_id: int
    """Identifier of the user who sent the query"""
    currency: str
    """Currency for the product price"""
    total_amount: int
    """Total price for the product, in the smallest units of the currency"""
    invoice_payload: bytes
    """Invoice payload"""
    shipping_option_id: str | None = None
    """Identifier of a shipping option chosen by the user; may be empty if not applicable"""
    order_info: OrderInfo | None = None
    """Information about the order; may be null"""

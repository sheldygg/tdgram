from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Address


@dataclass(kw_only=True)
class UpdateNewShippingQuery(BaseType):
    """
    A new incoming shipping query; for bots only. Only for invoices with flexible price
    """

    __type__: Literal["updateNewShippingQuery"] = "updateNewShippingQuery"

    id: int
    """Unique query identifier"""
    sender_user_id: int
    """Identifier of the user who sent the query"""
    invoice_payload: str
    """Invoice payload"""
    shipping_address: Address
    """User shipping address"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputInvoice, OrderInfo, ValidatedOrderInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class ValidateOrderInfo(BaseMethod):
    """
    Validates the order information provided by a user and returns the available shipping options for a flexible invoice
    """

    __type__: Literal["validateOrderInfo"] = "validateOrderInfo"
    __returning_type__ = ValidatedOrderInfo

    input_invoice: InputInvoice
    """The invoice"""
    order_info: OrderInfo | None = None
    """The order information, provided by the user; pass null if empty"""
    allow_save: bool
    """Pass true to save the order information"""

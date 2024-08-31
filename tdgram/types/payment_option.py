from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PaymentOption(BaseType):
    """
    Describes an additional payment option
    """

    __type__: Literal["paymentOption"] = "paymentOption"

    title: str
    """Title for the payment option"""
    url: str
    """Payment form URL to be opened in a web view"""

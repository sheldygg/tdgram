from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PaymentProviderOther(BaseType):
    """
    Some other payment provider, for which a web payment form must be shown
    """

    __type__: Literal["paymentProviderOther"] = "paymentProviderOther"

    url: str
    """Payment form URL"""

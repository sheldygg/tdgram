from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PaymentProviderSmartGlocal(BaseType):
    """
    Smart Glocal payment provider
    """

    __type__: Literal["paymentProviderSmartGlocal"] = "paymentProviderSmartGlocal"

    public_token: str
    """Public payment token"""
    tokenize_url: str
    """URL for sending card tokenization requests"""

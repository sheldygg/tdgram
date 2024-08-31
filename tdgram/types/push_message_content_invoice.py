from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PushMessageContentInvoice(BaseType):
    """
    A message with an invoice from a bot
    """

    __type__: Literal["pushMessageContentInvoice"] = "pushMessageContentInvoice"

    price: str
    """Product price"""
    is_pinned: bool
    """True, if the message is a pinned message with the specified content"""

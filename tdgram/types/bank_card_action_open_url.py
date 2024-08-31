from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BankCardActionOpenUrl(BaseType):
    """
    Describes an action associated with a bank card number
    """

    __type__: Literal["bankCardActionOpenUrl"] = "bankCardActionOpenUrl"

    text: str
    """Action text"""
    url: str
    """The URL to be opened"""

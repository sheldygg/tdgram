from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import BankCardActionOpenUrl


@dataclass(kw_only=True)
class BankCardInfo(BaseType):
    """
    Information about a bank card
    """

    __type__: Literal["bankCardInfo"] = "bankCardInfo"

    title: str
    """Title of the bank card description"""
    actions: list[BankCardActionOpenUrl]
    """Actions that can be done with the bank card number"""

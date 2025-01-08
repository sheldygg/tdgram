from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import UpgradedGift


@dataclass(kw_only=True)
class StarTransactionTypeGiftUpgrade(BaseType):
    """
    The transaction is an upgrade of a gift; for regular users only
    """

    __type__: Literal["starTransactionTypeGiftUpgrade"] = "starTransactionTypeGiftUpgrade"

    gift: UpgradedGift
    """The upgraded gift"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Gift


@dataclass(kw_only=True)
class StarTransactionTypeGiftSale(BaseType):
    """
    The transaction is a sale of a gift received from another user or bot; for regular users only
    """

    __type__: Literal["starTransactionTypeGiftSale"] = "starTransactionTypeGiftSale"

    user_id: int
    """Identifier of the user that sent the gift"""
    gift: Gift
    """The gift"""

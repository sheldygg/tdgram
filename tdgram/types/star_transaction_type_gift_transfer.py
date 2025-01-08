from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import UpgradedGift


@dataclass(kw_only=True)
class StarTransactionTypeGiftTransfer(BaseType):
    """
    The transaction is a transfer of an upgraded gift to another user; for regular users only
    """

    __type__: Literal["starTransactionTypeGiftTransfer"] = "starTransactionTypeGiftTransfer"

    user_id: int
    """Identifier of the user that received the gift"""
    gift: UpgradedGift
    """The gift"""

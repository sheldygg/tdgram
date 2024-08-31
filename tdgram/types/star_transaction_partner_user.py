from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Sticker


@dataclass(kw_only=True)
class StarTransactionPartnerUser(BaseType):
    """
    The transaction is a gift of Telegram Stars from another user
    """

    __type__: Literal["starTransactionPartnerUser"] = "starTransactionPartnerUser"

    user_id: int
    """Identifier of the user; 0 if the gift was anonymous"""
    sticker: Sticker | None = None
    """A sticker to be shown in the transaction information; may be null if unknown"""

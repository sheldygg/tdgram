from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Sticker


@dataclass(kw_only=True)
class StarTransactionTypeUserDeposit(BaseType):
    """
    The transaction is a deposit of Telegram Stars by another user; for regular users only
    """

    __type__: Literal["starTransactionTypeUserDeposit"] = "starTransactionTypeUserDeposit"

    user_id: int
    """Identifier of the user that gifted Telegram Stars; 0 if the user was anonymous"""
    sticker: Sticker | None = None
    """The sticker to be shown in the transaction information; may be null if unknown"""

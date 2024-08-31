from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import BotTransactionPurpose


@dataclass(kw_only=True)
class StarTransactionPartnerBot(BaseType):
    """
    The transaction is a transaction with a bot
    """

    __type__: Literal["starTransactionPartnerBot"] = "starTransactionPartnerBot"

    user_id: int
    """Identifier of the bot"""
    purpose: BotTransactionPurpose
    """Purpose of the transaction"""

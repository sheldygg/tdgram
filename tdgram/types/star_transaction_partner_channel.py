from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChannelTransactionPurpose


@dataclass(kw_only=True)
class StarTransactionPartnerChannel(BaseType):
    """
    The transaction is a transaction with a channel chat
    """

    __type__: Literal["starTransactionPartnerChannel"] = "starTransactionPartnerChannel"

    chat_id: int
    """Identifier of the chat"""
    purpose: ChannelTransactionPurpose
    """Purpose of the transaction"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatRevenueAmount


@dataclass(kw_only=True)
class UpdateChatRevenueAmount(BaseType):
    """
    The revenue earned from sponsored messages in a chat has changed. If chat revenue screen is opened, then getChatRevenueTransactions may be called to fetch new transactions
    """

    __type__: Literal["updateChatRevenueAmount"] = "updateChatRevenueAmount"

    chat_id: int
    """Identifier of the chat"""
    revenue_amount: ChatRevenueAmount
    """New amount of earned revenue"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatRevenueTransactions
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatRevenueTransactions(BaseMethod):
    """
    Returns the list of revenue transactions for a chat. Currently, this method can be used only for channels if supergroupFullInfo.can_get_revenue_statistics == true
    """

    __type__: Literal["getChatRevenueTransactions"] = "getChatRevenueTransactions"
    __returning_type__ = ChatRevenueTransactions

    chat_id: int
    """Chat identifier"""
    offset: int
    """Number of transactions to skip"""
    limit: int
    """The maximum number of transactions to be returned; up to 200"""

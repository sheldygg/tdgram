from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageSender, StarRevenueStatus


@dataclass(kw_only=True)
class UpdateStarRevenueStatus(BaseType):
    """
    The Telegram Star revenue earned by a bot or a chat has changed. If Telegram Star transaction screen of the chat is opened, then getStarTransactions may be called to fetch new transactions
    """

    __type__: Literal["updateStarRevenueStatus"] = "updateStarRevenueStatus"

    owner_id: MessageSender
    """Identifier of the owner of the Telegram Stars"""
    status: StarRevenueStatus
    """New Telegram Star revenue status"""

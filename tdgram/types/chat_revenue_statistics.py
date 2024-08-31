from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatRevenueAmount, StatisticalGraph


@dataclass(kw_only=True)
class ChatRevenueStatistics(BaseType):
    """
    A detailed statistics about revenue earned from sponsored messages in a chat
    """

    __type__: Literal["chatRevenueStatistics"] = "chatRevenueStatistics"

    revenue_by_hour_graph: StatisticalGraph
    """A graph containing amount of revenue in a given hour"""
    revenue_graph: StatisticalGraph
    """A graph containing amount of revenue"""
    revenue_amount: ChatRevenueAmount
    """Amount of earned revenue"""
    usd_rate: float
    """Current conversion rate of the cryptocurrency in which revenue is calculated to USD"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import StarRevenueStatus, StatisticalGraph


@dataclass(kw_only=True)
class StarRevenueStatistics(BaseType):
    """
    A detailed statistics about Telegram Stars earned by a bot or a chat
    """

    __type__: Literal["starRevenueStatistics"] = "starRevenueStatistics"

    revenue_by_day_graph: StatisticalGraph
    """A graph containing amount of revenue in a given day"""
    status: StarRevenueStatus
    """Telegram Star revenue status"""
    usd_rate: float
    """Current conversion rate of a Telegram Star to USD"""

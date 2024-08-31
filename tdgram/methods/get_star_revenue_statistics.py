from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MessageSender, StarRevenueStatistics
from .base import BaseMethod


@dataclass(kw_only=True)
class GetStarRevenueStatistics(BaseMethod):
    """
    Returns detailed Telegram Star revenue statistics
    """

    __type__: Literal["getStarRevenueStatistics"] = "getStarRevenueStatistics"
    __returning_type__ = StarRevenueStatistics

    owner_id: MessageSender
    """Identifier of the owner of the Telegram Stars; can be identifier of an owned bot, or identifier of a channel chat with supergroupFullInfo.can_get_star_revenue_statistics == true"""
    is_dark: bool
    """Pass true if a dark theme is used by the application"""

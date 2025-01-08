from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatRevenueStatistics
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatRevenueStatistics(BaseMethod):
    """
    Returns detailed revenue statistics about a chat. Currently, this method can be used only
    """

    __type__: Literal["getChatRevenueStatistics"] = "getChatRevenueStatistics"
    __returning_type__ = ChatRevenueStatistics

    chat_id: int
    """Chat identifier"""
    is_dark: bool
    """Pass true if a dark theme is used by the application"""

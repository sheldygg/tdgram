from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatEventIsAllHistoryAvailableToggled(BaseType):
    """
    The is_all_history_available setting of a supergroup was toggled
    """

    __type__: Literal["chatEventIsAllHistoryAvailableToggled"] = (
        "chatEventIsAllHistoryAvailableToggled"
    )

    is_all_history_available: bool
    """New value of is_all_history_available"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatStatisticsInviterInfo(BaseType):
    """
    Contains statistics about number of new members invited by a user
    """

    __type__: Literal["chatStatisticsInviterInfo"] = "chatStatisticsInviterInfo"

    user_id: int
    """User identifier"""
    added_member_count: int
    """Number of new members invited by the user"""

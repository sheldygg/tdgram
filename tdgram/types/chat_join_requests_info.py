from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatJoinRequestsInfo(BaseType):
    """
    Contains information about pending join requests for a chat
    """

    __type__: Literal["chatJoinRequestsInfo"] = "chatJoinRequestsInfo"

    total_count: int
    """Total number of pending join requests"""
    user_ids: list[int]
    """Identifiers of at most 3 users sent the newest pending join requests"""

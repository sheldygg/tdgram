from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatJoinRequest


@dataclass(kw_only=True)
class ChatJoinRequests(BaseType):
    """
    Contains a list of requests to join a chat
    """

    __type__: Literal["chatJoinRequests"] = "chatJoinRequests"

    total_count: int
    """Approximate total number of requests found"""
    requests: list[ChatJoinRequest]
    """List of the requests"""

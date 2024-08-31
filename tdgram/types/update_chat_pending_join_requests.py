from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatJoinRequestsInfo


@dataclass(kw_only=True)
class UpdateChatPendingJoinRequests(BaseType):
    """
    The chat pending join requests were changed
    """

    __type__: Literal["updateChatPendingJoinRequests"] = "updateChatPendingJoinRequests"

    chat_id: int
    """Chat identifier"""
    pending_join_requests: ChatJoinRequestsInfo | None = None
    """The new data about pending join requests; may be null"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatInviteLinkCounts
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatInviteLinkCounts(BaseMethod):
    """
    Returns the list of chat administrators with number of their invite links. Requires owner privileges in the chat
    """

    __type__: Literal["getChatInviteLinkCounts"] = "getChatInviteLinkCounts"
    __returning_type__ = ChatInviteLinkCounts

    chat_id: int
    """Chat identifier"""

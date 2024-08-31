from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Messages
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchChatRecentLocationMessages(BaseMethod):
    """
    Returns information about the recent locations of chat members that were sent to the chat. Returns up to 1 location message per user
    """

    __type__: Literal["searchChatRecentLocationMessages"] = "searchChatRecentLocationMessages"
    __returning_type__ = Messages

    chat_id: int
    """Chat identifier"""
    limit: int
    """The maximum number of messages to be returned"""

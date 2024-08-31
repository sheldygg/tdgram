from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleChatIsMarkedAsUnread(BaseMethod):
    """
    Changes the marked as unread state of a chat
    """

    __type__: Literal["toggleChatIsMarkedAsUnread"] = "toggleChatIsMarkedAsUnread"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    is_marked_as_unread: bool
    """New value of is_marked_as_unread"""

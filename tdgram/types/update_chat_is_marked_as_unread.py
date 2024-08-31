from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateChatIsMarkedAsUnread(BaseType):
    """
    A chat was marked as unread or was read
    """

    __type__: Literal["updateChatIsMarkedAsUnread"] = "updateChatIsMarkedAsUnread"

    chat_id: int
    """Chat identifier"""
    is_marked_as_unread: bool
    """New value of is_marked_as_unread"""

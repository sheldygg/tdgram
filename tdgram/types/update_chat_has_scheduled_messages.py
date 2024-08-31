from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateChatHasScheduledMessages(BaseType):
    """
    A chat's has_scheduled_messages field has changed
    """

    __type__: Literal["updateChatHasScheduledMessages"] = "updateChatHasScheduledMessages"

    chat_id: int
    """Chat identifier"""
    has_scheduled_messages: bool
    """New value of has_scheduled_messages"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class UnpinChatMessage(BaseMethod):
    """
    Removes a pinned message from a chat; requires can_pin_messages member right if the chat is a basic group or supergroup, or can_edit_messages administrator right if the chat is a channel
    """

    __type__: Literal["unpinChatMessage"] = "unpinChatMessage"
    __returning_type__ = Ok

    chat_id: int
    """Identifier of the chat"""
    message_id: int
    """Identifier of the removed pinned message"""

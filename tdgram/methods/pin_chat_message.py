from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class PinChatMessage(BaseMethod):
    """
    Pins a message in a chat. A message can be pinned only if messageProperties.can_be_pinned
    """

    __type__: Literal["pinChatMessage"] = "pinChatMessage"
    __returning_type__ = Ok

    chat_id: int
    """Identifier of the chat"""
    message_id: int
    """Identifier of the new pinned message"""
    disable_notification: bool
    """Pass true to disable notification about the pinned message. Notifications are always disabled in channels and private chats"""
    only_for_self: bool
    """Pass true to pin the message only for self; private chats only"""

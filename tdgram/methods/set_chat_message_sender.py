from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MessageSender, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetChatMessageSender(BaseMethod):
    """
    Selects a message sender to send messages in a chat
    """

    __type__: Literal["setChatMessageSender"] = "setChatMessageSender"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    message_sender_id: MessageSender
    """New message sender for the chat"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageSender


@dataclass(kw_only=True)
class UpdateChatMessageSender(BaseType):
    """
    The message sender that is selected to send messages in a chat has changed
    """

    __type__: Literal["updateChatMessageSender"] = "updateChatMessageSender"

    chat_id: int
    """Chat identifier"""
    message_sender_id: MessageSender | None = None
    """New value of message_sender_id; may be null if the user can't change message sender"""

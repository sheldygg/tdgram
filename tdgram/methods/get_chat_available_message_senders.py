from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatMessageSenders
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatAvailableMessageSenders(BaseMethod):
    """
    Returns the list of message sender identifiers, which can be used to send messages in a chat
    """

    __type__: Literal["getChatAvailableMessageSenders"] = "getChatAvailableMessageSenders"
    __returning_type__ = ChatMessageSenders

    chat_id: int
    """Chat identifier"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import AvailableReactions
from .base import BaseMethod


@dataclass(kw_only=True)
class GetMessageAvailableReactions(BaseMethod):
    """
    Returns reactions, which can be added to a message. The list can change after updateActiveEmojiReactions, updateChatAvailableReactions for the chat, or updateMessageInteractionInfo for the message
    """

    __type__: Literal["getMessageAvailableReactions"] = "getMessageAvailableReactions"
    __returning_type__ = AvailableReactions

    chat_id: int
    """Identifier of the chat to which the message belongs"""
    message_id: int
    """Identifier of the message"""
    row_size: int
    """Number of reaction per row, 5-25"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatAvailableReactions, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetChatAvailableReactions(BaseMethod):
    """
    Changes reactions, available in a chat. Available for basic groups, supergroups, and channels. Requires can_change_info member right
    """

    __type__: Literal["setChatAvailableReactions"] = "setChatAvailableReactions"
    __returning_type__ = Ok

    chat_id: int
    """Identifier of the chat"""
    available_reactions: ChatAvailableReactions
    """Reactions available in the chat. All explicitly specified emoji reactions must be active. In channel chats up to the chat's boost level custom emoji reactions can be explicitly specified"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatAvailableReactions


@dataclass(kw_only=True)
class UpdateChatAvailableReactions(BaseType):
    """
    The chat available reactions were changed
    """

    __type__: Literal["updateChatAvailableReactions"] = "updateChatAvailableReactions"

    chat_id: int
    """Chat identifier"""
    available_reactions: ChatAvailableReactions
    """The new reactions, available in the chat"""

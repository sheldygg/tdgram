from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatPosition


@dataclass(kw_only=True)
class UpdateChatPosition(BaseType):
    """
    The position of a chat in a chat list has changed. An updateChatLastMessage or updateChatDraftMessage update might be sent instead of the update
    """

    __type__: Literal["updateChatPosition"] = "updateChatPosition"

    chat_id: int
    """Chat identifier"""
    position: ChatPosition
    """New chat position. If new order is 0, then the chat needs to be removed from the list"""

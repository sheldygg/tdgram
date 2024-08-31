from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatPosition, Message


@dataclass(kw_only=True)
class UpdateChatLastMessage(BaseType):
    """
    The last message of a chat was changed
    """

    __type__: Literal["updateChatLastMessage"] = "updateChatLastMessage"

    chat_id: int
    """Chat identifier"""
    last_message: Message | None = None
    """The new last message in the chat; may be null if the last message became unknown. While the last message is unknown, new messages can be added to the chat without corresponding updateNewMessage update"""
    positions: list[ChatPosition]
    """The new chat positions in the chat lists"""

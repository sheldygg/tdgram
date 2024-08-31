from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import SharedChat


@dataclass(kw_only=True)
class MessageChatShared(BaseType):
    """
    The current user shared a chat, which was requested by the bot
    """

    __type__: Literal["messageChatShared"] = "messageChatShared"

    chat: SharedChat
    """The shared chat"""
    button_id: int
    """Identifier of the keyboard button with the request"""

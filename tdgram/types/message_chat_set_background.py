from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatBackground


@dataclass(kw_only=True)
class MessageChatSetBackground(BaseType):
    """
    A new background was set in the chat
    """

    __type__: Literal["messageChatSetBackground"] = "messageChatSetBackground"

    old_background_message_id: int
    """Identifier of the message with a previously set same background; 0 if none. Can be an identifier of a deleted message"""
    background: ChatBackground
    """The new background"""
    only_for_self: bool
    """True, if the background was set only for self"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageSender


@dataclass(kw_only=True)
class ChatMessageSender(BaseType):
    """
    Represents a message sender, which can be used to send messages in a chat
    """

    __type__: Literal["chatMessageSender"] = "chatMessageSender"

    sender: MessageSender
    """The message sender"""
    needs_premium: bool
    """True, if Telegram Premium is needed to use the message sender"""

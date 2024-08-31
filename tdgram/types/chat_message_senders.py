from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatMessageSender


@dataclass(kw_only=True)
class ChatMessageSenders(BaseType):
    """
    Represents a list of message senders, which can be used to send messages in a chat
    """

    __type__: Literal["chatMessageSenders"] = "chatMessageSenders"

    senders: list[ChatMessageSender]
    """List of available message senders"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageContent


@dataclass(kw_only=True)
class UpdateMessageContent(BaseType):
    """
    The message content has changed
    """

    __type__: Literal["updateMessageContent"] = "updateMessageContent"

    chat_id: int
    """Chat identifier"""
    message_id: int
    """Message identifier"""
    new_content: MessageContent
    """New message content"""

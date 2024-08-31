from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Message
from .base import BaseMethod


@dataclass(kw_only=True)
class GetCallbackQueryMessage(BaseMethod):
    """
    Returns information about a message with the callback button that originated a callback query; for bots only
    """

    __type__: Literal["getCallbackQueryMessage"] = "getCallbackQueryMessage"
    __returning_type__ = Message

    chat_id: int
    """Identifier of the chat the message belongs to"""
    message_id: int
    """Message identifier"""
    callback_query_id: int
    """Identifier of the callback query"""

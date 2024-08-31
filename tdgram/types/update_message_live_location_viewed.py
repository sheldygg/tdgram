from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateMessageLiveLocationViewed(BaseType):
    """
    A message with a live location was viewed. When the update is received, the application is supposed to update the live location
    """

    __type__: Literal["updateMessageLiveLocationViewed"] = "updateMessageLiveLocationViewed"

    chat_id: int
    """Identifier of the chat with the live location message"""
    message_id: int
    """Identifier of the message with live location"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StoryAreaTypeMessage(BaseType):
    """
    An area pointing to a message
    """

    __type__: Literal["storyAreaTypeMessage"] = "storyAreaTypeMessage"

    chat_id: int
    """Identifier of the chat with the message"""
    message_id: int
    """Identifier of the message"""

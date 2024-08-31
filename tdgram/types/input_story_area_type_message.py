from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputStoryAreaTypeMessage(BaseType):
    """
    An area pointing to a message
    """

    __type__: Literal["inputStoryAreaTypeMessage"] = "inputStoryAreaTypeMessage"

    chat_id: int
    """Identifier of the chat with the message. Currently, the chat must be a supergroup or a channel chat"""
    message_id: int
    """Identifier of the message. Use messageProperties.can_be_shared_in_story to check whether the message is suitable"""

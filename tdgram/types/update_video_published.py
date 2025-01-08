from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateVideoPublished(BaseType):
    """
    An automatically scheduled message with video has been successfully sent after conversion
    """

    __type__: Literal["updateVideoPublished"] = "updateVideoPublished"

    chat_id: int
    """Identifier of the chat with the message"""
    message_id: int
    """Identifier of the sent message"""

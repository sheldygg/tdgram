from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateMessageContentOpened(BaseType):
    """
    The message content was opened. Updates voice note messages to 'listened', video note messages to 'viewed' and starts the self-destruct timer
    """

    __type__: Literal["updateMessageContentOpened"] = "updateMessageContentOpened"

    chat_id: int
    """Chat identifier"""
    message_id: int
    """Message identifier"""

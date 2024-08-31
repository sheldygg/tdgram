from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class OpenMessageContent(BaseMethod):
    """
    Informs TDLib that the message content has been opened (e.g., the user has opened a photo, video, document, location or venue, or has listened to an audio file or voice note message).
    """

    __type__: Literal["openMessageContent"] = "openMessageContent"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier of the message"""
    message_id: int
    """Identifier of the message with the opened content"""

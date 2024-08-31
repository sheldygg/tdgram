from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Sticker
from .base import BaseMethod


@dataclass(kw_only=True)
class ClickAnimatedEmojiMessage(BaseMethod):
    """
    Informs TDLib that a message with an animated emoji was clicked by the user. Returns a big animated sticker to be played or a 404 error if usual animation needs to be played
    """

    __type__: Literal["clickAnimatedEmojiMessage"] = "clickAnimatedEmojiMessage"
    __returning_type__ = Sticker

    chat_id: int
    """Chat identifier of the message"""
    message_id: int
    """Identifier of the clicked message"""

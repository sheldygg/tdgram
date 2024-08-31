from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import EmojiStatus


@dataclass(kw_only=True)
class ChatEventEmojiStatusChanged(BaseType):
    """
    The chat emoji status was changed
    """

    __type__: Literal["chatEventEmojiStatusChanged"] = "chatEventEmojiStatusChanged"

    old_emoji_status: EmojiStatus | None = None
    """Previous emoji status; may be null if none"""
    new_emoji_status: EmojiStatus | None = None
    """New emoji status; may be null if none"""

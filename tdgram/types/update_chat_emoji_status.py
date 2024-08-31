from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import EmojiStatus


@dataclass(kw_only=True)
class UpdateChatEmojiStatus(BaseType):
    """
    Chat emoji status has changed
    """

    __type__: Literal["updateChatEmojiStatus"] = "updateChatEmojiStatus"

    chat_id: int
    """Chat identifier"""
    emoji_status: EmojiStatus | None = None
    """The new chat emoji status; may be null"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import EmojiStatuses
from .base import BaseMethod


@dataclass(kw_only=True)
class GetDisallowedChatEmojiStatuses(BaseMethod):
    """
    Returns the list of emoji statuses, which can't be used as chat emoji status, even they are from a sticker set with is_allowed_as_chat_emoji_status == true
    """

    __type__: Literal["getDisallowedChatEmojiStatuses"] = "getDisallowedChatEmojiStatuses"
    __returning_type__ = EmojiStatuses

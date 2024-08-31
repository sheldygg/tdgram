from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import EmojiStatuses
from .base import BaseMethod


@dataclass(kw_only=True)
class GetThemedChatEmojiStatuses(BaseMethod):
    """
    Returns up to 8 emoji statuses, which must be shown in the emoji status list for chats
    """

    __type__: Literal["getThemedChatEmojiStatuses"] = "getThemedChatEmojiStatuses"
    __returning_type__ = EmojiStatuses

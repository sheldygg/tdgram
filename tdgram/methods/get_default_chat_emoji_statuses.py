from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import EmojiStatuses
from .base import BaseMethod


@dataclass(kw_only=True)
class GetDefaultChatEmojiStatuses(BaseMethod):
    """
    Returns default emoji statuses for chats
    """

    __type__: Literal["getDefaultChatEmojiStatuses"] = "getDefaultChatEmojiStatuses"
    __returning_type__ = EmojiStatuses

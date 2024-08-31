from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class EmojiStatuses(BaseType):
    """
    Contains a list of custom emoji identifiers for emoji statuses
    """

    __type__: Literal["emojiStatuses"] = "emojiStatuses"

    custom_emoji_ids: list[int]
    """The list of custom emoji identifiers"""

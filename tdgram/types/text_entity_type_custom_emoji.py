from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TextEntityTypeCustomEmoji(BaseType):
    """
    A custom emoji. The text behind a custom emoji must be an emoji. Only premium users can use premium custom emoji
    """

    __type__: Literal["textEntityTypeCustomEmoji"] = "textEntityTypeCustomEmoji"

    custom_emoji_id: int
    """Unique identifier of the custom emoji"""

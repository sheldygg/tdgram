from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ReactionTypeCustomEmoji(BaseType):
    """
    A reaction with a custom emoji
    """

    __type__: Literal["reactionTypeCustomEmoji"] = "reactionTypeCustomEmoji"

    custom_emoji_id: int
    """Unique identifier of the custom emoji"""

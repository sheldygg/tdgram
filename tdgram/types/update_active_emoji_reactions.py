from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateActiveEmojiReactions(BaseType):
    """
    The list of active emoji reactions has changed
    """

    __type__: Literal["updateActiveEmojiReactions"] = "updateActiveEmojiReactions"

    emojis: list[str]
    """The new list of active emoji reactions"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ReactionTypeEmoji(BaseType):
    """
    A reaction with an emoji
    """

    __type__: Literal["reactionTypeEmoji"] = "reactionTypeEmoji"

    emoji: str
    """Text representation of the reaction"""

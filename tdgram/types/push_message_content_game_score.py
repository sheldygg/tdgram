from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PushMessageContentGameScore(BaseType):
    """
    A new high score was achieved in a game
    """

    __type__: Literal["pushMessageContentGameScore"] = "pushMessageContentGameScore"

    title: str
    """Game title, empty for pinned message"""
    score: int
    """New score, 0 for pinned message"""
    is_pinned: bool
    """True, if the message is a pinned message with the specified content"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PushMessageContentGame(BaseType):
    """
    A message with a game
    """

    __type__: Literal["pushMessageContentGame"] = "pushMessageContentGame"

    title: str
    """Game title, empty for pinned game message"""
    is_pinned: bool
    """True, if the message is a pinned message with the specified content"""

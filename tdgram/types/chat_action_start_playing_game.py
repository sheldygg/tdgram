from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatActionStartPlayingGame(BaseType):
    """
    The user has started to play a game
    """

    __type__: Literal["chatActionStartPlayingGame"] = "chatActionStartPlayingGame"

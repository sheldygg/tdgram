from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageGameScore(BaseType):
    """
    A new high score was achieved in a game
    """

    __type__: Literal["messageGameScore"] = "messageGameScore"

    game_message_id: int
    """Identifier of the message with the game, can be an identifier of a deleted message"""
    game_id: int
    """Identifier of the game; may be different from the games presented in the message with the game"""
    score: int
    """New score"""

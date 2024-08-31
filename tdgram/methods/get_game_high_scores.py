from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import GameHighScores
from .base import BaseMethod


@dataclass(kw_only=True)
class GetGameHighScores(BaseMethod):
    """
    Returns the high scores for a game and some part of the high score table in the range of the specified user; for bots only
    """

    __type__: Literal["getGameHighScores"] = "getGameHighScores"
    __returning_type__ = GameHighScores

    chat_id: int
    """The chat that contains the message with the game"""
    message_id: int
    """Identifier of the message"""
    user_id: int
    """User identifier"""

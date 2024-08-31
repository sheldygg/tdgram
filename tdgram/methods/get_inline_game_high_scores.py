from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import GameHighScores
from .base import BaseMethod


@dataclass(kw_only=True)
class GetInlineGameHighScores(BaseMethod):
    """
    Returns game high scores and some part of the high score table in the range of the specified user; for bots only
    """

    __type__: Literal["getInlineGameHighScores"] = "getInlineGameHighScores"
    __returning_type__ = GameHighScores

    inline_message_id: str
    """Inline message identifier"""
    user_id: int
    """User identifier"""

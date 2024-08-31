from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class GameHighScore(BaseType):
    """
    Contains one row of the game high score table
    """

    __type__: Literal["gameHighScore"] = "gameHighScore"

    position: int
    """Position in the high score table"""
    user_id: int
    """User identifier"""
    score: int
    """User score"""

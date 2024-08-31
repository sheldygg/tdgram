from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import GameHighScore


@dataclass(kw_only=True)
class GameHighScores(BaseType):
    """
    Contains a list of game high scores
    """

    __type__: Literal["gameHighScores"] = "gameHighScores"

    scores: list[GameHighScore]
    """A list of game high scores"""

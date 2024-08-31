from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Game


@dataclass(kw_only=True)
class InlineQueryResultGame(BaseType):
    """
    Represents information about a game
    """

    __type__: Literal["inlineQueryResultGame"] = "inlineQueryResultGame"

    id: str
    """Unique identifier of the query result"""
    game: Game
    """Game result"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Game


@dataclass(kw_only=True)
class MessageGame(BaseType):
    """
    A message with a game
    """

    __type__: Literal["messageGame"] = "messageGame"

    game: Game
    """The game description"""

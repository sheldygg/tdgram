from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputMessageGame(BaseType):
    """
    A message with a game; not supported for channels or secret chats
    """

    __type__: Literal["inputMessageGame"] = "inputMessageGame"

    bot_user_id: int
    """User identifier of the bot that owns the game"""
    game_short_name: str
    """Short name of the game"""

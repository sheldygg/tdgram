from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeGame(BaseType):
    """
    The link is a link to a game. Call searchPublicChat with the given bot username, check that the user is a bot,
    """

    __type__: Literal["internalLinkTypeGame"] = "internalLinkTypeGame"

    bot_username: str
    """Username of the bot that owns the game"""
    game_short_name: str
    """Short name of the game"""

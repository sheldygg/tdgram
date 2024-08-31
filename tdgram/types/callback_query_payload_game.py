from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CallbackQueryPayloadGame(BaseType):
    """
    The payload for a game callback button
    """

    __type__: Literal["callbackQueryPayloadGame"] = "callbackQueryPayloadGame"

    game_short_name: str
    """A short name of the game that was attached to the callback button"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BotCommand(BaseType):
    """
    Represents a command supported by a bot
    """

    __type__: Literal["botCommand"] = "botCommand"

    command: str
    """Text of the bot command"""
    description: str
    """Description of the bot command"""

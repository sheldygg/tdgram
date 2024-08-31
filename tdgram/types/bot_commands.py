from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import BotCommand


@dataclass(kw_only=True)
class BotCommands(BaseType):
    """
    Contains a list of bot commands
    """

    __type__: Literal["botCommands"] = "botCommands"

    bot_user_id: int
    """Bot's user identifier"""
    commands: list[BotCommand]
    """List of bot commands"""

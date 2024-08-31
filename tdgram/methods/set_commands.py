from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BotCommand, BotCommandScope, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetCommands(BaseMethod):
    """
    Sets the list of commands supported by the bot for the given user scope and language; for bots only
    """

    __type__: Literal["setCommands"] = "setCommands"
    __returning_type__ = Ok

    scope: BotCommandScope | None = None
    """The scope to which the commands are relevant; pass null to change commands in the default bot command scope"""
    language_code: str
    """A two-letter ISO 639-1 language code. If empty, the commands will be applied to all users from the given scope, for which language there are no dedicated commands"""
    commands: list[BotCommand]
    """List of the bot's commands"""

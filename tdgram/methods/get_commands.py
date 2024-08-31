from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BotCommands, BotCommandScope
from .base import BaseMethod


@dataclass(kw_only=True)
class GetCommands(BaseMethod):
    """
    Returns the list of commands supported by the bot for the given user scope and language; for bots only
    """

    __type__: Literal["getCommands"] = "getCommands"
    __returning_type__ = BotCommands

    scope: BotCommandScope | None = None
    """The scope to which the commands are relevant; pass null to get commands in the default bot command scope"""
    language_code: str
    """A two-letter ISO 639-1 language code or an empty string"""

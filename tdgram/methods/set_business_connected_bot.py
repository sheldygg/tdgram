from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BusinessConnectedBot, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetBusinessConnectedBot(BaseMethod):
    """
    Adds or changes business bot that is connected to the current user account
    """

    __type__: Literal["setBusinessConnectedBot"] = "setBusinessConnectedBot"
    __returning_type__ = Ok

    bot: BusinessConnectedBot
    """Connection settings for the bot"""

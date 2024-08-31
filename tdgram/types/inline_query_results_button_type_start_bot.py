from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InlineQueryResultsButtonTypeStartBot(BaseType):
    """
    Describes the button that opens a private chat with the bot and sends a start message to the bot with the given parameter
    """

    __type__: Literal["inlineQueryResultsButtonTypeStartBot"] = (
        "inlineQueryResultsButtonTypeStartBot"
    )

    parameter: str
    """The parameter for the bot start message"""

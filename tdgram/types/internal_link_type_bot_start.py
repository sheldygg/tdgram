from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeBotStart(BaseType):
    """
    The link is a link to a chat with a Telegram bot. Call searchPublicChat with the given bot username, check that the user is a bot, show START button in the chat with the bot,
    """

    __type__: Literal["internalLinkTypeBotStart"] = "internalLinkTypeBotStart"

    bot_username: str
    """Username of the bot"""
    start_parameter: str
    """The parameter to be passed to sendBotStartMessage"""
    autostart: bool
    """True, if sendBotStartMessage must be called automatically without showing the START button"""

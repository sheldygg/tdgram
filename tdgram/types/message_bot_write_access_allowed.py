from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import BotWriteAccessAllowReason


@dataclass(kw_only=True)
class MessageBotWriteAccessAllowed(BaseType):
    """
    The user allowed the bot to send messages
    """

    __type__: Literal["messageBotWriteAccessAllowed"] = "messageBotWriteAccessAllowed"

    reason: BotWriteAccessAllowReason
    """The reason why the bot was allowed to write messages"""

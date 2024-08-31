from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class AllowBotToSendMessages(BaseMethod):
    """
    Allows the specified bot to send messages to the user
    """

    __type__: Literal["allowBotToSendMessages"] = "allowBotToSendMessages"
    __returning_type__ = Ok

    bot_user_id: int
    """Identifier of the target bot"""

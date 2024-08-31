from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class CanBotSendMessages(BaseMethod):
    """
    Checks whether the specified bot can send messages to the user. Returns a 404 error if can't and the access can be granted by call to allowBotToSendMessages
    """

    __type__: Literal["canBotSendMessages"] = "canBotSendMessages"
    __returning_type__ = Ok

    bot_user_id: int
    """Identifier of the target bot"""

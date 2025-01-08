from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SellGift(BaseMethod):
    """
    Sells a gift received by the current user for Telegram Stars
    """

    __type__: Literal["sellGift"] = "sellGift"
    __returning_type__ = Ok

    sender_user_id: int
    """Identifier of the user that sent the gift"""
    message_id: int
    """Identifier of the message with the gift in the chat with the user"""

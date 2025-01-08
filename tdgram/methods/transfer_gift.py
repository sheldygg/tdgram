from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class TransferGift(BaseMethod):
    """
    Sends a gift upgraded by the current user to another user
    """

    __type__: Literal["transferGift"] = "transferGift"
    __returning_type__ = Ok

    sender_user_id: int
    """Identifier of the user that sent the gift"""
    message_id: int
    """Identifier of the message with the upgraded gift in the chat with the user"""
    receiver_user_id: int
    """Identifier of the user that will receive the gift"""
    star_count: int
    """The amount of Telegram Stars required for the transfer"""

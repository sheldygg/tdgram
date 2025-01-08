from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class RemovePendingPaidMessageReactions(BaseMethod):
    """
    Removes all pending paid reactions on a message
    """

    __type__: Literal["removePendingPaidMessageReactions"] = "removePendingPaidMessageReactions"
    __returning_type__ = Ok

    chat_id: int
    """Identifier of the chat to which the message belongs"""
    message_id: int
    """Identifier of the message"""

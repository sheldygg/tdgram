from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateMessageSendAcknowledged(BaseType):
    """
    A request to send a message has reached the Telegram server. This doesn't mean that the message will be sent successfully.
    """

    __type__: Literal["updateMessageSendAcknowledged"] = "updateMessageSendAcknowledged"

    chat_id: int
    """The chat identifier of the sent message"""
    message_id: int
    """A temporary message identifier"""

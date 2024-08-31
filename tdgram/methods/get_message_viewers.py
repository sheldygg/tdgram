from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MessageViewers
from .base import BaseMethod


@dataclass(kw_only=True)
class GetMessageViewers(BaseMethod):
    """
    Returns viewers of a recent outgoing message in a basic group or a supergroup chat. For video notes and voice notes only users, opened content of the message, are returned. The method can be called if messageProperties.can_get_viewers == true
    """

    __type__: Literal["getMessageViewers"] = "getMessageViewers"
    __returning_type__ = MessageViewers

    chat_id: int
    """Chat identifier"""
    message_id: int
    """Identifier of the message"""

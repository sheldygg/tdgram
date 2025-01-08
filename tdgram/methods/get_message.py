from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Message
from .base import BaseMethod


@dataclass(kw_only=True)
class GetMessage(BaseMethod):
    """
    Returns information about a message. Returns a 404 error if the message doesn't exist
    """

    __type__: Literal["getMessage"] = "getMessage"
    __returning_type__ = Message

    chat_id: int
    """Identifier of the chat the message belongs to"""
    message_id: int
    """Identifier of the message to get"""

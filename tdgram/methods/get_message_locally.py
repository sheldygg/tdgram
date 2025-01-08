from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Message
from .base import BaseMethod


@dataclass(kw_only=True)
class GetMessageLocally(BaseMethod):
    """
    Returns information about a message, if it is available without sending network request. Returns a 404 error if message isn't available locally. This is an offline request
    """

    __type__: Literal["getMessageLocally"] = "getMessageLocally"
    __returning_type__ = Message

    chat_id: int
    """Identifier of the chat the message belongs to"""
    message_id: int
    """Identifier of the message to get"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Messages
from .base import BaseMethod


@dataclass(kw_only=True)
class GetMessages(BaseMethod):
    """
    Returns information about messages. If a message is not found, returns null on the corresponding position of the result
    """

    __type__: Literal["getMessages"] = "getMessages"
    __returning_type__ = Messages

    chat_id: int
    """Identifier of the chat the messages belong to"""
    message_ids: list[int]
    """Identifiers of the messages to get"""

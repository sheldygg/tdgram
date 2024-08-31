from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class UnpinAllMessageThreadMessages(BaseMethod):
    """
    Removes all pinned messages from a forum topic; requires can_pin_messages member right in the supergroup
    """

    __type__: Literal["unpinAllMessageThreadMessages"] = "unpinAllMessageThreadMessages"
    __returning_type__ = Ok

    chat_id: int
    """Identifier of the chat"""
    message_thread_id: int
    """Message thread identifier in which messages will be unpinned"""

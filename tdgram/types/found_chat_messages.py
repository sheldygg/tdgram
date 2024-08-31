from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Message


@dataclass(kw_only=True)
class FoundChatMessages(BaseType):
    """
    Contains a list of messages found by a search in a given chat
    """

    __type__: Literal["foundChatMessages"] = "foundChatMessages"

    total_count: int
    """Approximate total number of messages found; -1 if unknown"""
    messages: list[Message]
    """List of messages"""
    next_from_message_id: int
    """The offset for the next request. If 0, there are no more results"""

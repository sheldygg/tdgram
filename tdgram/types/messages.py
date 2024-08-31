from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Message


@dataclass(kw_only=True)
class Messages(BaseType):
    """
    Contains a list of messages
    """

    __type__: Literal["messages"] = "messages"

    total_count: int
    """Approximate total number of messages found"""
    messages: list[Message]
    """List of messages; messages may be null"""

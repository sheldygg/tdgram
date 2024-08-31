from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Message


@dataclass(kw_only=True)
class FoundMessages(BaseType):
    """
    Contains a list of messages found by a search
    """

    __type__: Literal["foundMessages"] = "foundMessages"

    total_count: int
    """Approximate total number of messages found; -1 if unknown"""
    messages: list[Message]
    """List of messages"""
    next_offset: str
    """The offset for the next request. If empty, then there are no more results"""

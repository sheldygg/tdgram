from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PublicForward


@dataclass(kw_only=True)
class PublicForwards(BaseType):
    """
    Represents a list of public forwards and reposts as a story of a message or a story
    """

    __type__: Literal["publicForwards"] = "publicForwards"

    total_count: int
    """Approximate total number of messages and stories found"""
    forwards: list[PublicForward]
    """List of found public forwards and reposts"""
    next_offset: str
    """The offset for the next request. If empty, then there are no more results"""

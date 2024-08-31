from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessagePosition


@dataclass(kw_only=True)
class MessagePositions(BaseType):
    """
    Contains a list of message positions
    """

    __type__: Literal["messagePositions"] = "messagePositions"

    total_count: int
    """Total number of messages found"""
    positions: list[MessagePosition]
    """List of message positions"""

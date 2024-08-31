from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessagePosition(BaseType):
    """
    Contains information about a message in a specific position
    """

    __type__: Literal["messagePosition"] = "messagePosition"

    position: int
    """0-based message position in the full list of suitable messages"""
    message_id: int
    """Message identifier"""
    date: int
    """Point in time (Unix timestamp) when the message was sent"""

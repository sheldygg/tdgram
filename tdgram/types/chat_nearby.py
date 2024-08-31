from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatNearby(BaseType):
    """
    Describes a chat located nearby
    """

    __type__: Literal["chatNearby"] = "chatNearby"

    chat_id: int
    """Chat identifier"""
    distance: int
    """Distance to the chat location, in meters"""

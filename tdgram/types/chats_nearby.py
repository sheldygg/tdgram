from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatNearby


@dataclass(kw_only=True)
class ChatsNearby(BaseType):
    """
    Represents a list of chats located nearby
    """

    __type__: Literal["chatsNearby"] = "chatsNearby"

    users_nearby: list[ChatNearby]
    """List of users nearby"""
    supergroups_nearby: list[ChatNearby]
    """List of location-based supergroups nearby"""

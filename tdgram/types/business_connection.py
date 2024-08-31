from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BusinessConnection(BaseType):
    """
    Describes a connection of the bot with a business account
    """

    __type__: Literal["businessConnection"] = "businessConnection"

    id: str
    """Unique identifier of the connection"""
    user_id: int
    """Identifier of the business user that created the connection"""
    user_chat_id: int
    """Chat identifier of the private chat with the user"""
    date: int
    """Point in time (Unix timestamp) when the connection was established"""
    can_reply: bool
    """True, if the bot can send messages to the connected user; false otherwise"""
    is_enabled: bool
    """True, if the connection is enabled; false otherwise"""

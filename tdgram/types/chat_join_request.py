from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatJoinRequest(BaseType):
    """
    Describes a user that sent a join request and waits for administrator approval
    """

    __type__: Literal["chatJoinRequest"] = "chatJoinRequest"

    user_id: int
    """User identifier"""
    date: int
    """Point in time (Unix timestamp) when the user sent the join request"""
    bio: str
    """A short bio of the user"""

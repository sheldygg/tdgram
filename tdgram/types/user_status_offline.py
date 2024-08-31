from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UserStatusOffline(BaseType):
    """
    The user is offline
    """

    __type__: Literal["userStatusOffline"] = "userStatusOffline"

    was_online: int
    """Point in time (Unix timestamp) when the user was last online"""

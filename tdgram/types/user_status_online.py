from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UserStatusOnline(BaseType):
    """
    The user is online
    """

    __type__: Literal["userStatusOnline"] = "userStatusOnline"

    expires: int
    """Point in time (Unix timestamp) when the user's online status will expire"""

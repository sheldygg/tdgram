from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatTypePrivate(BaseType):
    """
    An ordinary chat with a user
    """

    __type__: Literal["chatTypePrivate"] = "chatTypePrivate"

    user_id: int
    """User identifier"""

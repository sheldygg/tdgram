from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class Chats(BaseType):
    """
    Represents a list of chats
    """

    __type__: Literal["chats"] = "chats"

    total_count: int
    """Approximate total number of chats found"""
    chat_ids: list[int]
    """List of chat identifiers"""

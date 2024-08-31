from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TopChatCategoryUsers(BaseType):
    """
    A category containing frequently used private chats with non-bot users
    """

    __type__: Literal["topChatCategoryUsers"] = "topChatCategoryUsers"

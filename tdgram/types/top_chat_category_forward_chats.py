from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TopChatCategoryForwardChats(BaseType):
    """
    A category containing frequently used chats used to forward messages
    """

    __type__: Literal["topChatCategoryForwardChats"] = "topChatCategoryForwardChats"

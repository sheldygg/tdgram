from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatAvailableReactionsAll(BaseType):
    """
    All reactions are available in the chat, excluding the paid reaction and custom reactions in channel chats
    """

    __type__: Literal["chatAvailableReactionsAll"] = "chatAvailableReactionsAll"

    max_reaction_count: int
    """The maximum allowed number of reactions per message; 1-11"""

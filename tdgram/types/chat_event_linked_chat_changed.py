from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatEventLinkedChatChanged(BaseType):
    """
    The linked chat of a supergroup was changed
    """

    __type__: Literal["chatEventLinkedChatChanged"] = "chatEventLinkedChatChanged"

    old_linked_chat_id: int
    """Previous supergroup linked chat identifier"""
    new_linked_chat_id: int
    """New supergroup linked chat identifier"""

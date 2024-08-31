from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageChatDeleteMember(BaseType):
    """
    A chat member was deleted
    """

    __type__: Literal["messageChatDeleteMember"] = "messageChatDeleteMember"

    user_id: int
    """User identifier of the deleted chat member"""

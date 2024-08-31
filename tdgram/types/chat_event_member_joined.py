from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatEventMemberJoined(BaseType):
    """
    A new member joined the chat
    """

    __type__: Literal["chatEventMemberJoined"] = "chatEventMemberJoined"

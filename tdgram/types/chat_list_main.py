from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatListMain(BaseType):
    """
    A main list of chats
    """

    __type__: Literal["chatListMain"] = "chatListMain"

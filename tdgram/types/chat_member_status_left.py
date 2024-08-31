from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatMemberStatusLeft(BaseType):
    """
    The user or the chat is not a chat member
    """

    __type__: Literal["chatMemberStatusLeft"] = "chatMemberStatusLeft"

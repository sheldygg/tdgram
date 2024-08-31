from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageSourceChatList(BaseType):
    """
    The message is from a chat list or a forum topic list
    """

    __type__: Literal["messageSourceChatList"] = "messageSourceChatList"

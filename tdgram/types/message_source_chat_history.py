from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageSourceChatHistory(BaseType):
    """
    The message is from a chat history
    """

    __type__: Literal["messageSourceChatHistory"] = "messageSourceChatHistory"

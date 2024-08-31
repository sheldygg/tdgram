from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatActionTyping(BaseType):
    """
    The user is typing a message
    """

    __type__: Literal["chatActionTyping"] = "chatActionTyping"

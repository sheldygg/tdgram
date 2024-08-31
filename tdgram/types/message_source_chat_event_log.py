from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageSourceChatEventLog(BaseType):
    """
    The message is from a chat event log
    """

    __type__: Literal["messageSourceChatEventLog"] = "messageSourceChatEventLog"

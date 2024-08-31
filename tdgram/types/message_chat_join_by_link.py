from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageChatJoinByLink(BaseType):
    """
    A new member joined the chat via an invite link
    """

    __type__: Literal["messageChatJoinByLink"] = "messageChatJoinByLink"

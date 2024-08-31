from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PushMessageContentChatJoinByLink(BaseType):
    """
    A new member joined the chat via an invite link
    """

    __type__: Literal["pushMessageContentChatJoinByLink"] = "pushMessageContentChatJoinByLink"

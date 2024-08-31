from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PushMessageContentChatJoinByRequest(BaseType):
    """
    A new member was accepted to the chat by an administrator
    """

    __type__: Literal["pushMessageContentChatJoinByRequest"] = (
        "pushMessageContentChatJoinByRequest"
    )

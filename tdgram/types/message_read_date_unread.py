from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageReadDateUnread(BaseType):
    """
    The message is unread yet
    """

    __type__: Literal["messageReadDateUnread"] = "messageReadDateUnread"

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateMessageIsPinned(BaseType):
    """
    The message pinned state was changed
    """

    __type__: Literal["updateMessageIsPinned"] = "updateMessageIsPinned"

    chat_id: int
    """Chat identifier"""
    message_id: int
    """The message identifier"""
    is_pinned: bool
    """True, if the message is pinned"""

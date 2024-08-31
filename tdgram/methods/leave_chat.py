from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class LeaveChat(BaseMethod):
    """
    Removes the current user from chat members. Private and secret chats can't be left using this method
    """

    __type__: Literal["leaveChat"] = "leaveChat"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""

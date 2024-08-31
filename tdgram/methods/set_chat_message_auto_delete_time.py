from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetChatMessageAutoDeleteTime(BaseMethod):
    """
    Changes the message auto-delete or self-destruct (for secret chats) time in a chat. Requires change_info administrator right in basic groups, supergroups and channels
    """

    __type__: Literal["setChatMessageAutoDeleteTime"] = "setChatMessageAutoDeleteTime"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    message_auto_delete_time: int
    """New time value, in seconds; unless the chat is secret, it must be from 0 up to 365 * 86400 and be divisible by 86400. If 0, then messages aren't deleted automatically"""

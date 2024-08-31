from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageChatSetMessageAutoDeleteTime(BaseType):
    """
    The auto-delete or self-destruct timer for messages in the chat has been changed
    """

    __type__: Literal["messageChatSetMessageAutoDeleteTime"] = (
        "messageChatSetMessageAutoDeleteTime"
    )

    message_auto_delete_time: int
    """New value auto-delete or self-destruct time, in seconds; 0 if disabled"""
    from_user_id: int
    """If not 0, a user identifier, which default setting was automatically applied"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateChatDefaultDisableNotification(BaseType):
    """
    The value of the default disable_notification parameter, used when a message is sent to the chat, was changed
    """

    __type__: Literal["updateChatDefaultDisableNotification"] = (
        "updateChatDefaultDisableNotification"
    )

    chat_id: int
    """Chat identifier"""
    default_disable_notification: bool
    """The new default_disable_notification value"""

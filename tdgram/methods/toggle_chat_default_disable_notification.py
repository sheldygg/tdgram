from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleChatDefaultDisableNotification(BaseMethod):
    """
    Changes the value of the default disable_notification parameter, used when a message is sent to a chat
    """

    __type__: Literal["toggleChatDefaultDisableNotification"] = (
        "toggleChatDefaultDisableNotification"
    )
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    default_disable_notification: bool
    """New value of default_disable_notification"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatNotificationSettings, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetChatNotificationSettings(BaseMethod):
    """
    Changes the notification settings of a chat. Notification settings of a chat with the current user (Saved Messages) can't be changed
    """

    __type__: Literal["setChatNotificationSettings"] = "setChatNotificationSettings"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    notification_settings: ChatNotificationSettings
    """New notification settings for the chat. If the chat is muted for more than 366 days, it is considered to be muted forever"""

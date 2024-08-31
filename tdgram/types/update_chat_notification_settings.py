from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatNotificationSettings


@dataclass(kw_only=True)
class UpdateChatNotificationSettings(BaseType):
    """
    Notification settings for a chat were changed
    """

    __type__: Literal["updateChatNotificationSettings"] = "updateChatNotificationSettings"

    chat_id: int
    """Chat identifier"""
    notification_settings: ChatNotificationSettings
    """The new notification settings"""

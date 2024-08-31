from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Notification, NotificationGroupType


@dataclass(kw_only=True)
class UpdateNotificationGroup(BaseType):
    """
    A list of active notifications in a notification group has changed
    """

    __type__: Literal["updateNotificationGroup"] = "updateNotificationGroup"

    notification_group_id: int
    """Unique notification group identifier"""
    type: NotificationGroupType
    """New type of the notification group"""
    chat_id: int
    """Identifier of a chat to which all notifications in the group belong"""
    notification_settings_chat_id: int
    """Chat identifier, which notification settings must be applied to the added notifications"""
    notification_sound_id: int
    """Identifier of the notification sound to be played; 0 if sound is disabled"""
    total_count: int
    """Total number of unread notifications in the group, can be bigger than number of active notifications"""
    added_notifications: list[Notification]
    """List of added group notifications, sorted by notification identifier"""
    removed_notification_ids: list[int]
    """Identifiers of removed group notifications, sorted by notification identifier"""

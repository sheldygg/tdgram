from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Notification, NotificationGroupType


@dataclass(kw_only=True)
class NotificationGroup(BaseType):
    """
    Describes a group of notifications
    """

    __type__: Literal["notificationGroup"] = "notificationGroup"

    id: int
    """Unique persistent auto-incremented from 1 identifier of the notification group"""
    type: NotificationGroupType
    """Type of the group"""
    chat_id: int
    """Identifier of a chat to which all notifications in the group belong"""
    total_count: int
    """Total number of active notifications in the group"""
    notifications: list[Notification]
    """The list of active notifications"""

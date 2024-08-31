from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import NotificationSettingsScope, ScopeNotificationSettings


@dataclass(kw_only=True)
class UpdateScopeNotificationSettings(BaseType):
    """
    Notification settings for some type of chats were updated
    """

    __type__: Literal["updateScopeNotificationSettings"] = "updateScopeNotificationSettings"

    scope: NotificationSettingsScope
    """Types of chats for which notification settings were updated"""
    notification_settings: ScopeNotificationSettings
    """The new notification settings"""

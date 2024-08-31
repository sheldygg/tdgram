from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import NotificationSettingsScope, Ok, ScopeNotificationSettings
from .base import BaseMethod


@dataclass(kw_only=True)
class SetScopeNotificationSettings(BaseMethod):
    """
    Changes notification settings for chats of a given type
    """

    __type__: Literal["setScopeNotificationSettings"] = "setScopeNotificationSettings"
    __returning_type__ = Ok

    scope: NotificationSettingsScope
    """Types of chats for which to change the notification settings"""
    notification_settings: ScopeNotificationSettings
    """The new notification settings for the given scope"""

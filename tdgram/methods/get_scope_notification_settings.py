from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import NotificationSettingsScope, ScopeNotificationSettings
from .base import BaseMethod


@dataclass(kw_only=True)
class GetScopeNotificationSettings(BaseMethod):
    """
    Returns the notification settings for chats of a given type
    """

    __type__: Literal["getScopeNotificationSettings"] = "getScopeNotificationSettings"
    __returning_type__ = ScopeNotificationSettings

    scope: NotificationSettingsScope
    """Types of chats for which to return the notification settings information"""

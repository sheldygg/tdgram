from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class NotificationSettingsScopePrivateChats(BaseType):
    """
    Notification settings applied to all private and secret chats when the corresponding chat setting has a default value
    """

    __type__: Literal["notificationSettingsScopePrivateChats"] = (
        "notificationSettingsScopePrivateChats"
    )

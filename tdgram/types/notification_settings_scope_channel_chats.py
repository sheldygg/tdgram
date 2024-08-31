from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class NotificationSettingsScopeChannelChats(BaseType):
    """
    Notification settings applied to all channel chats when the corresponding chat setting has a default value
    """

    __type__: Literal["notificationSettingsScopeChannelChats"] = (
        "notificationSettingsScopeChannelChats"
    )

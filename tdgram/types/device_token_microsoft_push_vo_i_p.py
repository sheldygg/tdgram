from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class DeviceTokenMicrosoftPushVoIP(BaseType):
    """
    A token for Microsoft Push Notification Service VoIP channel
    """

    __type__: Literal["deviceTokenMicrosoftPushVoIP"] = "deviceTokenMicrosoftPushVoIP"

    channel_uri: str | None = None
    """Push notification channel URI; may be empty to deregister a device"""

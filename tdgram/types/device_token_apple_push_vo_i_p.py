from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class DeviceTokenApplePushVoIP(BaseType):
    """
    A token for Apple Push Notification service VoIP notifications
    """

    __type__: Literal["deviceTokenApplePushVoIP"] = "deviceTokenApplePushVoIP"

    device_token: str | None = None
    """Device token; may be empty to deregister a device"""
    is_app_sandbox: bool
    """True, if App Sandbox is enabled"""
    encrypt: bool
    """True, if push notifications must be additionally encrypted"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class DeviceTokenApplePush(BaseType):
    """
    A token for Apple Push Notification service
    """

    __type__: Literal["deviceTokenApplePush"] = "deviceTokenApplePush"

    device_token: str | None = None
    """Device token; may be empty to deregister a device"""
    is_app_sandbox: bool
    """True, if App Sandbox is enabled"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class DeviceTokenFirebaseCloudMessaging(BaseType):
    """
    A token for Firebase Cloud Messaging
    """

    __type__: Literal["deviceTokenFirebaseCloudMessaging"] = "deviceTokenFirebaseCloudMessaging"

    token: str | None = None
    """Device registration token; may be empty to deregister a device"""
    encrypt: bool
    """True, if push notifications must be additionally encrypted"""

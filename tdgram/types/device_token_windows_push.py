from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class DeviceTokenWindowsPush(BaseType):
    """
    A token for Windows Push Notification Services
    """

    __type__: Literal["deviceTokenWindowsPush"] = "deviceTokenWindowsPush"

    access_token: str | None = None
    """The access token that will be used to send notifications; may be empty to deregister a device"""

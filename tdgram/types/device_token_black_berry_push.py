from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class DeviceTokenBlackBerryPush(BaseType):
    """
    A token for BlackBerry Push Service
    """

    __type__: Literal["deviceTokenBlackBerryPush"] = "deviceTokenBlackBerryPush"

    token: str | None = None
    """Token; may be empty to deregister a device"""

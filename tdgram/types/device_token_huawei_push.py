from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class DeviceTokenHuaweiPush(BaseType):
    """
    A token for HUAWEI Push Service
    """

    __type__: Literal["deviceTokenHuaweiPush"] = "deviceTokenHuaweiPush"

    token: str | None = None
    """Device registration token; may be empty to deregister a device"""
    encrypt: bool
    """True, if push notifications must be additionally encrypted"""

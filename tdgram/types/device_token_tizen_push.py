from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class DeviceTokenTizenPush(BaseType):
    """
    A token for Tizen Push Service
    """

    __type__: Literal["deviceTokenTizenPush"] = "deviceTokenTizenPush"

    reg_id: str | None = None
    """Push service registration identifier; may be empty to deregister a device"""

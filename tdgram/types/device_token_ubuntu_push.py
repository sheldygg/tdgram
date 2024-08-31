from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class DeviceTokenUbuntuPush(BaseType):
    """
    A token for Ubuntu Push Client service
    """

    __type__: Literal["deviceTokenUbuntuPush"] = "deviceTokenUbuntuPush"

    token: str | None = None
    """Token; may be empty to deregister a device"""

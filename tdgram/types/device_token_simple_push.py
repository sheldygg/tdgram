from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class DeviceTokenSimplePush(BaseType):
    """
    A token for Simple Push API for Firefox OS
    """

    __type__: Literal["deviceTokenSimplePush"] = "deviceTokenSimplePush"

    endpoint: str | None = None
    """Absolute URL exposed by the push service where the application server can send push messages; may be empty to deregister a device"""

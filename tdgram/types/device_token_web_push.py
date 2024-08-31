from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class DeviceTokenWebPush(BaseType):
    """
    A token for web Push API
    """

    __type__: Literal["deviceTokenWebPush"] = "deviceTokenWebPush"

    endpoint: str | None = None
    """Absolute URL exposed by the push service where the application server can send push messages; may be empty to deregister a device"""
    p256dh_base64url: str
    """Base64url-encoded P-256 elliptic curve Diffie-Hellman public key"""
    auth_base64url: str
    """Base64url-encoded authentication secret"""

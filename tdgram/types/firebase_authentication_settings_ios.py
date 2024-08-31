from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class FirebaseAuthenticationSettingsIos(BaseType):
    """
    Settings for Firebase Authentication in the official iOS application
    """

    __type__: Literal["firebaseAuthenticationSettingsIos"] = "firebaseAuthenticationSettingsIos"

    device_token: str
    """Device token from Apple Push Notification service"""
    is_app_sandbox: bool
    """True, if App Sandbox is enabled"""

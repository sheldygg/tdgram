from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import DeviceToken, PushReceiverId
from .base import BaseMethod


@dataclass(kw_only=True)
class RegisterDevice(BaseMethod):
    """
    Registers the currently used device for receiving push notifications. Returns a globally unique identifier of the push notification subscription
    """

    __type__: Literal["registerDevice"] = "registerDevice"
    __returning_type__ = PushReceiverId

    device_token: DeviceToken
    """Device token"""
    other_user_ids: list[int]
    """List of user identifiers of other users currently using the application"""

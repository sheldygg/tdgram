from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateHavePendingNotifications(BaseType):
    """
    Describes whether there are some pending notification updates. Can be used to prevent application from killing, while there are some pending notifications
    """

    __type__: Literal["updateHavePendingNotifications"] = "updateHavePendingNotifications"

    have_delayed_notifications: bool
    """True, if there are some delayed notification updates, which will be sent soon"""
    have_unreceived_notifications: bool
    """True, if there can be some yet unreceived notifications, which are being fetched from the server"""

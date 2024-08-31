from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class NotificationGroupTypeMessages(BaseType):
    """
    A group containing notifications of type notificationTypeNewMessage and notificationTypeNewPushMessage with ordinary unread messages
    """

    __type__: Literal["notificationGroupTypeMessages"] = "notificationGroupTypeMessages"

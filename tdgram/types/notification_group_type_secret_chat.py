from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class NotificationGroupTypeSecretChat(BaseType):
    """
    A group containing a notification of type notificationTypeNewSecretChat
    """

    __type__: Literal["notificationGroupTypeSecretChat"] = "notificationGroupTypeSecretChat"

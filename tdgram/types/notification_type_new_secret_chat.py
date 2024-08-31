from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class NotificationTypeNewSecretChat(BaseType):
    """
    New secret chat was created
    """

    __type__: Literal["notificationTypeNewSecretChat"] = "notificationTypeNewSecretChat"

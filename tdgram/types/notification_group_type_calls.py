from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class NotificationGroupTypeCalls(BaseType):
    """
    A group containing notifications of type notificationTypeNewCall
    """

    __type__: Literal["notificationGroupTypeCalls"] = "notificationGroupTypeCalls"

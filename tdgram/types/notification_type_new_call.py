from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class NotificationTypeNewCall(BaseType):
    """
    New call was received
    """

    __type__: Literal["notificationTypeNewCall"] = "notificationTypeNewCall"

    call_id: int
    """Call identifier"""

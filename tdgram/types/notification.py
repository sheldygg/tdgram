from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import NotificationType


@dataclass(kw_only=True)
class Notification(BaseType):
    """
    Contains information about a notification
    """

    __type__: Literal["notification"] = "notification"

    id: int
    """Unique persistent identifier of this notification"""
    date: int
    """Notification date"""
    is_silent: bool
    """True, if the notification was explicitly sent without sound"""
    type: NotificationType
    """Notification type"""

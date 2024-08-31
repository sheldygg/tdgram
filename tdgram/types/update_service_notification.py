from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageContent


@dataclass(kw_only=True)
class UpdateServiceNotification(BaseType):
    """
    A service notification from the server was received. Upon receiving this the application must show a popup with the content of the notification
    """

    __type__: Literal["updateServiceNotification"] = "updateServiceNotification"

    type: str
    """Notification type. If type begins with 'AUTH_KEY_DROP_', then two buttons 'Cancel' and 'Log out' must be shown under notification; if user presses the second, all local data must be destroyed using Destroy method"""
    content: MessageContent
    """Notification content"""
